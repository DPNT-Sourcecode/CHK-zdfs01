
class CheckoutSolution:

    # skus = unicode string
    def checkout(self, skus):
        # Reject non strings
        if not isinstance(skus, str):
            return -1 
        # Reject illegal input
        if any(ch not in "ABCD" for ch in skus):
            return -1


