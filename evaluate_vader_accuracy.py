"""
Evaluate the accuracy and throughput of the VADER sentiment classifier
using the NLTK movie_reviews dataset (2,000 labeled reviews).
"""

import time
from collections import Counter

from nltk import download
from nltk.corpus import movie_reviews
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer


def ensure_movie_reviews():
    """Download the NLTK movie_reviews corpus if it is not available."""
    try:
        movie_reviews.categories()
    except LookupError:
        download("movie_reviews")


def evaluate_vader_on_movie_reviews(threshold: float = 0.05):
    """Return metrics for VADER evaluated on the movie_reviews corpus."""
    ensure_movie_reviews()
    analyzer = SentimentIntensityAnalyzer()

    true_labels = []
    pred_labels = []

    start = time.time()
    for fileid in movie_reviews.fileids():
        text = movie_reviews.raw(fileid)
        compound = analyzer.polarity_scores(text)["compound"]
        pred = 1 if compound >= threshold else 0  # 1=positive, 0=negative
        true = 1 if movie_reviews.categories(fileid)[0] == "pos" else 0
        pred_labels.append(pred)
        true_labels.append(true)
    end = time.time()

    n = len(true_labels)
    correct = sum(int(t == p) for t, p in zip(true_labels, pred_labels))
    accuracy = correct / n

    tp = sum(1 for t, p in zip(true_labels, pred_labels) if t == 1 and p == 1)
    tn = sum(1 for t, p in zip(true_labels, pred_labels) if t == 0 and p == 0)
    fp = sum(1 for t, p in zip(true_labels, pred_labels) if t == 0 and p == 1)
    fn = sum(1 for t, p in zip(true_labels, pred_labels) if t == 1 and p == 0)

    def safe_div(num, denom):
        return num / denom if denom else 0.0

    precision_pos = safe_div(tp, tp + fp)
    recall_pos = safe_div(tp, tp + fn)
    f1_pos = safe_div(2 * precision_pos * recall_pos, precision_pos + recall_pos)

    precision_neg = safe_div(tn, tn + fn)
    recall_neg = safe_div(tn, tn + fp)
    f1_neg = safe_div(2 * precision_neg * recall_neg, precision_neg + recall_neg)

    throughput = safe_div(n, end - start)

    return {
        "samples": n,
        "accuracy": accuracy,
        "positives": {"precision": precision_pos, "recall": recall_pos, "f1": f1_pos},
        "negatives": {"precision": precision_neg, "recall": recall_neg, "f1": f1_neg},
        "confusion": {"tp": tp, "tn": tn, "fp": fp, "fn": fn},
        "runtime_sec": end - start,
        "throughput_docs_per_sec": throughput,
    }


if __name__ == "__main__":
    metrics = evaluate_vader_on_movie_reviews()
    print(f"Evaluated {metrics['samples']} labeled movie reviews.")
    print(f"Accuracy: {metrics['accuracy']:.4f}")
    print(
        "Positive precision/recall/F1: "
        f"{metrics['positives']['precision']:.4f} / "
        f"{metrics['positives']['recall']:.4f} / "
        f"{metrics['positives']['f1']:.4f}"
    )
    print(
        "Negative precision/recall/F1: "
        f"{metrics['negatives']['precision']:.4f} / "
        f"{metrics['negatives']['recall']:.4f} / "
        f"{metrics['negatives']['f1']:.4f}"
    )
    confusion = metrics["confusion"]
    print(
        f"Confusion matrix -> TP:{confusion['tp']}  FP:{confusion['fp']}  "
        f"TN:{confusion['tn']}  FN:{confusion['fn']}"
    )
    print(
        f"Runtime: {metrics['runtime_sec']:.2f} s  "
        f"Throughput: {metrics['throughput_docs_per_sec']:.2f} documents/sec"
    )

