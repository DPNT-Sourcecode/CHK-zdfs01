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

        # Offers 
        total += (a // 3) * 130 + (a % 3) * 50 # A: 3 for 130, else 50 each
        total += (b // 2) * 45 + (b % 2) * 30  # B: 2 for 45, else 30 each
        total += c * 20                        # C: 20 each
        total += d *15                         # D: 15 each

        



