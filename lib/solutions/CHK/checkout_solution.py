from collections import Counter

class CheckoutSolution:

    # skus = unicode string
    def checkout(self, skus: str | None) -> int:
        """
        Calculate the total checkout price for the given SKU string.

        Pricing and offers:
        +------+-------+---------------------------------+
        | Item | Price | Special offers                  |
        +------+-------+---------------------------------+
        | A    | 50    | 3A for 130, 5A for 200          |
        | B    | 30    | 2B for 45                       |
        | C    | 20    |                                 |
        | D    | 15    |                                 |
        | E    | 40    | 2E get one B free               |
        | F    | 10    | 2F get one F free               |
        | G    | 20    |                                 |
        | H    | 10    | 5H for 45, 10H for 80           |
        | I    | 35    |                                 |
        | J    | 60    |                                 |
        | K    | 70    | 2K for 120                      |
        | L    | 90    |                                 |
        | M    | 15    |                                 |
        | N    | 40    | 3N get one M free               |
        | O    | 10    |                                 |
        | P    | 50    | 5P for 200                      |
        | Q    | 30    | 3Q for 80                       |
        | R    | 50    | 3R get one Q free               |
        | S    | 20    | buy any 3 of (S,T,X,Y,Z) for 45 |
        | T    | 20    | buy any 3 of (S,T,X,Y,Z) for 45 |
        | U    | 40    | 3U get one U free               |
        | V    | 50    | 2V for 90, 3V for 130           |
        | W    | 20    |                                 |
        | X    | 17    | buy any 3 of (S,T,X,Y,Z) for 45 |
        | Y    | 20    | buy any 3 of (S,T,X,Y,Z) for 45 |
        | Z    | 21    | buy any 3 of (S,T,X,Y,Z) for 45 |
        +------+-------+---------------------------------+
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

        # === PRIORTY 1 ===
        # Inter-items promotional discounts

        # E offer: 2E get one B free
        e = counts.get("E", 0)
        b = counts.get("B", 0)
        freebie_b = (e // 2)
        b = max(0, b - freebie_b)
        total += e * 40

        # N offer: 3N get one M free
        n = counts.get("N", 0)
        m = counts.get("M", 0)
        freebie_m = (n // 3)
        m = max(0, m - freebie_m)
        total += n * 40

        # R offer: 3R get one Q free
        r = counts.get("R", 0)
        q = counts.get("Q", 0)
        freebie_q = (r // 3)
        q = max(0, q - freebie_q)
        total += r * 50

        # === PRIORITY 2 ===
        # Items with BOGOFF promotional discounts

        # F offer: 2F get one free so you need 3F for price of 2F
        f = counts.get ("F", 0)
        total += (f // 3) * 20 + (f % 3) * 10

        # U offer: 3U get one free so you need 4U for price of 3U
        u = counts.get ("U", 0)
        total += (u // 4) * 120 + (u % 4) * 40

        # === PRIORITY 3 ===
        # Items with multi-tiered promotional discounts

        # A offer: 5A for 200, 3A for 130, else 50 each
        a = counts.get("A", 0)
        total += (a // 5) * 200
        remainder_a = a % 5
        total += (remainder_a // 3) * 130
        total += (remainder_a % 3) * 50

        # H offer: 10H for 80, 5H for 45, else 10 each
        h = counts.get("H", 0)
        total += (h // 10) * 80
        remainder_h = h % 10
        total += (remainder_h // 5) * 45
        total += (remainder_h % 5) * 10

        # V offer: 3V for 130, 2V for 90, else 50 each
        v = counts.get("V", 0)
        total += (v // 3) * 130
        remainder_v = v % 3
        total += (remainder_v // 2) * 90
        total += (remainder_v % 2) * 50

        # === PRIORITY 4 ===
        # Items with basic-tiered promotional discounts 

        # B offer: 2B for 45, else 30 (after deductions)
        total += (b // 2) * 45 + (b % 2) * 30

        # K offer: 2K for 150, else 80
        k = counts.get("K", 0)
        total += (k // 2) * 150 + (k % 2) * 80

        # P offer: 5P for 200, else 50
        p = counts.get("P", 0)
        total += (p // 5) * 200 + (p % 5) * 50

        # Q offer: 3Q for 80, else 30 (after deductions)
        total += (q // 3) * 80 + (q % 3) * 30

        # === PRIORITY 5 ===
        # Items with no offers

        total += counts.get("C", 0) * 20
        total += counts.get("D", 0) * 15
        total += counts.get("G", 0) * 20
        total += counts.get("I", 0) * 35
        total += counts.get("J", 0) * 60
        total += counts.get("L", 0) * 90
        total += m * 15
        total += counts.get("O", 0) * 10
        total += counts.get("S", 0) * 30
        total += counts.get("T", 0) * 20
        total += counts.get("W", 0) * 20
        total += counts.get("X", 0) * 90
        total += counts.get("Y", 0) * 10
        total += counts.get("Z", 0) * 50

        return total
    
"""
We will need some complex handling to deal with the new offers
There is a new group discount for (S,T,X,Y,Z)
 
Changes:
- K price change 70, offer 2K for 120
- X price change 17
- S price change 20
- Z price change 21
- Group offer: Any (S,T,X,Y,Z) for 45

We will need to try and sort the group discount for the 


"""