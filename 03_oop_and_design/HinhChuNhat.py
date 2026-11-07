class HinhChuNhat:
    def __init__(self, chieu_dai: float, chieu_rong: float) -> None:
        self._chieu_dai = chieu_dai
        self._chieu_rong = chieu_rong
        
    @property
    def chieu_dai(self) -> float:
        return self._chieu_dai
    @chieu_dai.setter
    def chieu_dai(self, value: float) -> None:
        if value <= 0:
            raise ValueError("Chiều dài phải lớn hơn 0")
        self._chieu_dai = value
        
    @property
    def chieu_rong(self) -> float:
        return self._chieu_rong
    @chieu_rong.setter
    def chieu_rong(self, value: float) -> None:
        if value <= 0:
            raise ValueError("Chiều rộng phải lớn hơn 0")
        self._chieu_rong = value
            
    def tinh_dien_tich(self) -> float:
        return self.chieu_dai * self.chieu_rong
    def tinh_chu_vi(self) -> float:
        return (self.chieu_dai + self.chieu_rong) * 2
        
    def __str__(self) -> str:
        return f"Hình chữ nhật: chiều dài = {self._chieu_dai}, chiều rộng = {self._chieu_rong}, diện tích = {self.tinh_dien_tich()}, chu vi = {self.tinh_chu_vi()}"
def main()-> None:
    dai = float(input("Nhập chiều dài: "))
    rong = float(input("Nhập chiều rộng: "))
    hcn = HinhChuNhat(dai, rong)
    print(hcn)
if __name__ == "__main__":
    main()