from collections import Counter

class CheckoutSolution:

    # skus = unicode string
    def checkout(self, skus: str | None) -> int:
        """
        Calculate the total checkout price for the given SKU string.

        Pricing and offers:
        +------+-------+------------------------+
        | Item | Price | Special offers         |
        +------+-------+------------------------+
        | A    | 50    | 3A for 130, 5A for 200 |
        | B    | 30    | 2B for 45              |
        | C    | 20    |                        |
        | D    | 15    |                        |
        | E    | 40    | 2E get one B free      |
        | F    | 10    | 2F get one F free      |
        | G    | 20    |                        |
        | H    | 10    | 5H for 45, 10H for 80  |
        | I    | 35    |                        |
        | J    | 60    |                        |
        | K    | 80    | 2K for 150             |
        | L    | 90    |                        |
        | M    | 15    |                        |
        | N    | 40    | 3N get one M free      |
        | O    | 10    |                        |
        | P    | 50    | 5P for 200             |
        | Q    | 30    | 3Q for 80              |
        | R    | 50    | 3R get one Q free      |
        | S    | 30    |                        |
        | T    | 20    |                        |
        | U    | 40    | 3U get one U free      |
        | V    | 50    | 2V for 90, 3V for 130  |
        | W    | 20    |                        |
        | X    | 90    |                        |
        | Y    | 10    |                        |
        | Z    | 50    |                        |
        +------+-------+------------------------+

        Args:
            skus: A string of SKU letters representing items in the basket
        
        Returns:
            The total checkout value as an integer or -1 for invalid input
        
        """

        # Reject non strings
        if not isinstance(skus, str):
            return -1 
        # Reject illegal input (A-Z only)
        if any(ch not in "ABCDEFGHIJKLMNOPQRSTUVWXYZ" for ch in skus):
            return -1
        
        counts = Counter(skus)

        total = 0

        # 
        # Determine the best inter-item promotional discounts before anything else

        # E offer: 2E get one B free
        # We want to apply this first because it reduces B count
        freebie_b = (e // 2)
        b = max(0, b - freebie_b)

        # E pricing is 40 each
        total += e * 40

        # F offer: 2F get one free so you need 3F for price of 2F
        total += (f // 3) * 20
        total += (f % 3) * 10

        # A offer: 5A for 200, 3A for 130, else 50 each
        # We need to apply larger offer first because it favours the customer
        total += (a // 5) * 200
        remainder_a = a % 5
        total += (remainder_a // 3) * 130
        total += (remainder_a % 3) * 50

        # B offer: 2B for 45, else 30 each (post free B dediction)
        total += (b // 2) * 45 + (b % 2) * 30

        # C: 20 each
        total += c * 20

        # D: 15 each
        total += d *15  










        return total




