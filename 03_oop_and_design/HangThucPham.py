from datetime import date, timedelta
class HangThucPham:
    def __init__(
        self,
        MaHang: str,
        tenHang: str = "Chưa xác định",
        donGia: float = 0.0,
        ngaySX: date | None = None,
        ngayHH: date | None = None,
)-> None:
        if not MaHang or not MaHang.strip():
            self._MaHang = "MH_DEFAULT"
        else:
            self._MaHang = MaHang.strip()
        self.tenHang = tenHang
        self.donGia =  donGia
        today =  date.today()
        tomorrow = today + timedelta(days =1)
        safe_nsx = ngaySX if ngaySX is not None else today
        safe_hh = ngayHH if ngayHH is not None else tomorrow
        
        if safe_hh > safe_nsx:
            self._ngay_san_xuat = safe_nsx
            self._ngay_het_han = safe_hh
        else:
            self._ngay_san_xuat = today
            self._ngay_het_han = tomorrow
           
    @property
    def MaHang(self) -> str:
        return self._MaHang
    @property
    def tenHang(self) -> str:
        return self._tenHang
    @tenHang.setter
    def tenHang(self, value: str) ->None:
        if not value or not value.strip():
            self._tenHang = "Chưa xác định"
        else:
            self._tenHang = value.strip()
            
    @property
    def donGia(self) -> float:
        return self._donGia
    @donGia.setter 
    def donGia(self, value: float) -> None:
        if value >0:
            self._donGia = value
        else:
            self._donGia = 0.0
    
    @property 
    def ngay_san_xuat(self) -> date:
        return self._ngay_san_xuat
    @ngay_san_xuat.setter 
    def ngay_san_xuat(self, value: date) -> None:
        if value < self._ngay_het_han:
            self._ngay_san_xuat = value
        else:
            self._ngay_san_xuat = date.today()
        
    @property
    def ngay_het_han(self) -> date:
        return self._ngay_het_han
    @ngay_het_han.setter
    def ngay_het_han(self, value: date) -> None:
        if value > self._ngay_san_xuat:
            self._ngay_het_han = value
        else:
            self._ngay_het_han = self._ngay_san_xuat + timedelta(days=1)
            
    def kiem_tra_het_han(self) -> bool:
        return self._ngay_het_han < date.today()
    def __str__(self) -> str:

        gia_str = f"{self.donGia:,.0f} đ"

        nsx_str = self.ngay_san_xuat.strftime("%d/%m/%Y")
        nhd_str = self.ngay_het_han.strftime("%d/%m/%Y")
        
        ghi_chu = "Hết hạn" if self.kiem_tra_het_han() else ""

        return (
            f"Mã: {self._MaHang:<8} | Tên: {self.tenHang:<15} | "
            f"Giá: {gia_str:>12} | NSX: {nsx_str} | HSD: {nhd_str} | {ghi_chu}"
        )


def main() -> None:
    print("--- KIỂM NGHIỆM LỚP HÀNG THỰC PHẨM ---")
    
    sp1 = HangThucPham(MaHang="MH01")

    sp2 = HangThucPham(
        MaHang="MH02", 
        tenHang="Sữa tươi Mộc Châu", 
        donGia=35000, 
        ngaySX=date(2026, 11, 10), 
        ngayHH=date(2026, 11, 20)
    )
    
    sp3 = HangThucPham(
        MaHang="MH03", 
        tenHang="", 
        donGia=-5000, 
        ngaySX=date(2026, 12, 31), 
        ngayHH=date(2026, 1, 1)
    )
    
    sp4 = HangThucPham(
        MaHang="MH04",
        tenHang="Bánh mì",
        donGia=15000,
        ngaySX=date(2026, 11, 1),
        ngayHH=date(2026, 11, 5)
    )

    print(sp1)
    print(sp2)
    print(sp3)
    print(sp4)


if __name__ == "__main__":
    main()
    
    
        