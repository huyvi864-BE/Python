class Account:
    lai_suat: float = 0.035
    def __init__(
        self,
        so_tai_khoan: int = 0,
        ten_tai_khoan: str = "Chưa cập nhật",
        so_tien: float = 50.0
    )-> None:
        self._so_tai_khoan = so_tai_khoan
        self._ten_tai_khoan = ten_tai_khoan
        self._so_tien = so_tien
        
    @property
    def so_tai_khoan(self)-> int:
        return self._so_tai_khoan
    @so_tai_khoan.setter
    def so_tai_khoan(self, value : int)->None:
        self._so_tai_khoan = value
    
    @property
    def ten_tai_khoan(self) -> str:
        return self._ten_tai_khoan
    
    @ten_tai_khoan.setter
    def ten_tai_khoan(self, value : str) -> None:
        self._ten_tai_khoan
    @property
    def so_tien(self) -> float:
        return self._so_tien
    @so_tien.setter
    def so_tien(self, value: float) -> None:
        if value < 0:
            raise ValueError("Số tiền trong tài khoản không được âm!")
        self._so_tien = value
    
    def nap_tien(self, so_tien_nap: float) -> bool:
        if so_tien_nap <= 0:
            print(f"[{self.so_tai_khoan}] Lỗi nạp tiền: Số tiền nạp phải lớn hơn 0.")
            return False
        self._so_tien += so_tien_nap
        print(f"[{self.so_tai_khoan}] Giao dịch thành công: Nạp {so_tien_nap:,.2f}đ")
        return True

    def rut_tien(self, so_tien_rut: float, phi_rut_tien: float = 0.0) -> bool:
        if so_tien_rut <= 0:
            print(f"[{self.so_tai_khoan}] Lỗi rút tiền: Số tiền rút phải lớn hơn 0.")
            return False
            
        tong_tien_tru = so_tien_rut + phi_rut_tien
        if self._so_tien < tong_tien_tru:
            print(f"[{self.so_tai_khoan}] Giao dịch thất bại: Số dư không đủ (Cần: {tong_tien_tru:,.2f}đ).")
            return False
            
        self._so_tien -= tong_tien_tru
        print(f"[{self.so_tai_khoan}] Giao dịch thành công: Rút {so_tien_rut:,.2f}đ (Phí: {phi_rut_tien:,.2f}đ)")
        return True

    def dao_han(self) -> None:
        tien_lai = self._so_tien * Account.lai_suat
        self._so_tien += tien_lai
        print(f"[{self.so_tai_khoan}] Đã đáo hạn: Cộng tiền lãi {tien_lai:,.2f}đ")

    def chuyen_khoan(self, tai_khoan_dich: "Account", so_tien_chuyen: float) -> bool:
        print(f"\n--- Đang thực hiện chuyển khoản từ [{self.so_tai_khoan}] sang [{tai_khoan_dich.so_tai_khoan}] ---")
        if self.rut_tien(so_tien_chuyen, phi_rut_tien=0.0):
            tai_khoan_dich.nap_tien(so_tien_chuyen)
            print("=> Chuyển khoản hoàn tất!")
            return True
        print("=> Chuyển khoản thất bại!")
        return False

    def __str__(self) -> str:
        so_tien_dinh_dang = f"{self.so_tien:,.2f} VNĐ"
        return f"STK: {self.so_tai_khoan:<12} | Chủ thẻ: {self.ten_tai_khoan:<20} | Số dư: {so_tien_dinh_dang:>20}"


def main() -> None:
    acc1 = Account(so_tai_khoan=111222, ten_tai_khoan="Vi Quang Huy")
    
    acc2 = Account(so_tai_khoan=999888, ten_tai_khoan="Nguyen Van A", so_tien=5000000.0)

    print("--- TRẠNG THÁI BAN ĐẦU ---")
    print(acc1)
    print(acc2)
    print("\n--- GIAO DỊCH TÀI KHOẢN 1 ---")
    acc1.nap_tien(1000000)
    acc1.rut_tien(200000, 5000) 
    acc1.dao_han()      

    acc2.chuyen_khoan(acc1, 1500000)

    print("\n--- TRẠNG THÁI SAU GIAO DỊCH ---")
    print(acc1)
    print(acc2)


if __name__ == "__main__":
    main()
               
        
    