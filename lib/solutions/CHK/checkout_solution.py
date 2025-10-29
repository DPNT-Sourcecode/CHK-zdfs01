from collections import Counter

class CheckoutSolution:

    # skus = unicode string
    def checkout(self, skus):
        # Reject non strings
        if not isinstance(skus, str):
            return -1 
        # Reject illegal input
        if any(ch not in "ABCD" for ch in skus):
            return -1
        
        counts = Counter(skus)
        a = counts.get("A", 0)
        b = counts.get("B", 0)
        c = counts.get("C", 0)
        d = counts.get("D", 0)

        total = 0





