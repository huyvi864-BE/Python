"""
Module: 02_ex_quan_ly_sinh_vien.py
"""

class SinhVien:

    def __init__(
        self, 
        ma_sv: int = 0, 
        ho_ten: str = "", 
        diem_lt: float = 0.0, 
        diem_th: float = 0.0
    ) -> None:
        self._ma_sv = ma_sv
        self._ho_ten = ho_ten
        self._diem_lt = diem_lt
        self._diem_th = diem_th
        
    @property
    def ma_sv(self) -> int:
        return self._ma_sv

    @ma_sv.setter
    def ma_sv(self, value: int) -> None:
        self._ma_sv = value

    @property
    def ho_ten(self) -> str:
        return self._ho_ten

    @ho_ten.setter
    def ho_ten(self, value: str) -> None:
        self._ho_ten = value

    @property
    def diem_lt(self) -> float:
        return self._diem_lt

    @diem_lt.setter
    def diem_lt(self, value: float) -> None:
        if value < 0 or value > 10:
            raise ValueError("Điểm lý thuyết phải từ 0 đến 10")
        self._diem_lt = value

    @property
    def diem_th(self) -> float:
        return self._diem_th

    @diem_th.setter
    def diem_th(self, value: float) -> None:
        if value < 0 or value > 10:
            raise ValueError("Điểm thực hành phải từ 0 đến 10")
        self._diem_th = value

    def tinh_diem_tb(self) -> float:
        return (self.diem_lt + self.diem_th) / 2

    def __str__(self) -> str:
        return (
            f"{self.ma_sv:<10} | {self.ho_ten:<22} | "
            f"{self.diem_lt:<8.2f} | {self.diem_th:<8.2f} | "
            f"{self.tinh_diem_tb():<8.2f}"
        )


def main() -> None:
    sv1 = SinhVien(ma_sv=20211234, ho_ten="Vi Quang Huy", diem_lt=9.5, diem_th=9.0)

    sv2 = SinhVien(ma_sv=20215678, ho_ten="Nguyen Van A", diem_lt=8.0, diem_th=8.5)

    sv3 = SinhVien()
    print("--- NHẬP THÔNG TIN SINH VIÊN 3 ---")
    try:
        sv3.ma_sv = int(input("Nhập mã sinh viên: "))
        sv3.ho_ten = input("Nhập họ tên: ")
        sv3.diem_lt = float(input("Nhập điểm Lý thuyết: "))
        sv3.diem_th = float(input("Nhập điểm Thực hành: "))
    except ValueError as e:
        print(f"Lỗi nhập liệu: Dữ liệu không hợp lệ. ({e})")
        return
    print("\n" + "="*70)
    print(f"{'MSSV':<10} | {'Họ tên':<22} | {'Điểm LT':<8} | {'Điểm TH':<8} | {'Điểm TB':<8}")
    print("-" * 70)
    print(sv1)
    print(sv2)
    print(sv3)
    print("="*70)


if __name__ == "__main__":
    main()