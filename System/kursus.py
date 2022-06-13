class kursus():

    def __init__(self, kursusnavn: str, kursusnr: int):
        self.kursusnavn = kursusnavn
        self.kursusnr = kursusnr

    def getkursusnavn(self):
        return self.kursusnavn

    def getkursusnr(self):
        return self.kursusnr
