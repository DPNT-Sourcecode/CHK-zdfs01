from collections import Counter

class CheckoutSolution:

    # skus = unicode string
    def checkout(self, skus: str | None) -> int:
        """This function does XYZ"""

        # Reject non strings
        if not isinstance(skus, str):
            return -1 
        # Reject illegal input
        if any(ch not in "ABCDE" for ch in skus):
            return -1
        


        counts = Counter(skus)
        a = counts.get("A", 0)
        b = counts.get("B", 0)
        c = counts.get("C", 0)
        d = counts.get("D", 0)
        e = counts.get("E", 0)

        total = 0

        # E offer: 2E get one B free
        # We want to apply this first because it reduces B count
        freebie_b = (e // 2)
        b = max(0, b - freebie_b)

        # E pricing is 40 each
        total += e * 40

        # A offer: 5A for 200, 3A for 130, else 50 each
        # We need to apply larger offer first because it favours the customer
        total += (a // 5) * 200
        remainder_a = a % 5
        total += (remainder_a // 3) * 130
        total += (remainder_a % 3) * 50

        # B offer: 2B for 45, else 30 each (post free B dediction)
        total += (b // 2) * 45
        









        # Offers 
        total += (a // 3) * 130 + (a % 3) * 50 # A: 3 for 130, else 50 each
        total += (b // 2) * 45 + (b % 2) * 30  # B: 2 for 45, else 30 each
        total += c * 20                        # C: 20 each
        total += d *15                         # D: 15 each

        return total



