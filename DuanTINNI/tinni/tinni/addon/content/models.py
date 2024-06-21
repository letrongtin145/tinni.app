from django.db import models
from django.contrib.auth.models import User
import json

# from tinni.addon.hrm.models import Staffs, Departments
# from erp.addons.contacts.models import Contacts


class ContentLocal(models.Model):
    class Meta:
        db_table = "content_local"
        # default_permissions = ()
        # permissions = [
        #     ("add_cartdetail", "sale_manager - Thêm sản phẩm vào đơn hàng"),
        #     ("change_cartdetail", "sale_manager - Sửa sản phẩm trong đơn hàng"),
        #     ("delete_cartdetail", "sale_manager - Xoá sản phẩm trong đơn hàng"),
        #     ("view_cartdetail", "sale_manager - Xem sản phẩm trong đơn hàng"),
        #     ("detail_cartdetail", "sale_manager - Xem chi tiết sản phẩm trong đơn hàng"),
        #     ("view_cartdetail_report", "sale_manager - Xem báo cáo sản phẩm trong đơn hàng"),
        #     ("view_cartdetail_all", "sale_manager - Xem tất cả sản phẩm trong đơn hàng"),
        #     ("view_cartdetail_staff", "sale_manager - Nhân viên Quản lý, Tạo sản phẩm trong đơn hàng"),
        #     ("view_cartdetail_manager", "sale_manager - Giám sát Quản lý, Tạo sản phẩm trong đơn hàng"),
        # ]

    # ID khóa chính
    content_local_id = models.AutoField(primary_key=True, help_text='ID Khoá chính')   
    # tên tài liệu
    content_local_name = models.TextField(max_length=200, null=True, blank=True, help_text='Tên danh mục, kiểu input')
    # mô tả sơ lượt về tài liệu (sẽ được hiển thị dưới tên tài liệu trong hệ thống xem dispatch_send)
    content_local_description = models.TextField(max_length=1000, null=True, blank=True,
                                             help_text='Mô tả chi tiết, kiểu textarea')

    # trạng thái
    content_local_enable = models.BooleanField(null=True,
                                           blank=True)  # , help_text='Trạng thái: True - Đang quản lý; False - Không còn quản lý'
    content_local_status = models.BooleanField(null=True, blank=True,
                                           default=True)  # , help_text='Trạng thái: True - đang hoạt động; False - đã xóa'

    content_local_user_created = models.ForeignKey(User, related_name='ContentLocal_content_local_user_created',
                                               on_delete=models.SET_NULL, null=True, blank=True)
    content_local_user_updated = models.ForeignKey(User, related_name='ContentLocal_content_local_user_updated',
                                               on_delete=models.SET_NULL, null=True, blank=True)

    # Thời gian tạo dữ liệu, tự động điền theo giờ hệ thống
    content_local_created_at = models.DateTimeField(auto_now_add=True)
    # Thời gian cập nhật - thay đổi dữ liệu, tự động điền theo giờ hệ thống
    content_local_updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.content_local_name


class Content(models.Model):
    class Meta:
        db_table = "content"
        # default_permissions = ()
        # permissions = [
        #     ("add_cartdetail", "sale_manager - Thêm sản phẩm vào đơn hàng"),
        #     ("change_cartdetail", "sale_manager - Sửa sản phẩm trong đơn hàng"),
        #     ("delete_cartdetail", "sale_manager - Xoá sản phẩm trong đơn hàng"),
        #     ("view_cartdetail", "sale_manager - Xem sản phẩm trong đơn hàng"),
        #     ("detail_cartdetail", "sale_manager - Xem chi tiết sản phẩm trong đơn hàng"),
        #     ("view_cartdetail_report", "sale_manager - Xem báo cáo sản phẩm trong đơn hàng"),
        #     ("view_cartdetail_all", "sale_manager - Xem tất cả sản phẩm trong đơn hàng"),
        #     ("view_cartdetail_staff", "sale_manager - Nhân viên Quản lý, Tạo sản phẩm trong đơn hàng"),
        #     ("view_cartdetail_manager", "sale_manager - Giám sát Quản lý, Tạo sản phẩm trong đơn hàng"),
        # ]

    # ID khóa chính
    content_id = models.AutoField(primary_key=True, help_text='ID Khoá chính')   
    # tên tài liệu
    content_name = models.TextField(max_length=200, null=True, blank=True, help_text='Tên danh mục, kiểu input')
    # mô tả sơ lượt về tài liệu (sẽ được hiển thị dưới tên tài liệu trong hệ thống xem dispatch_send)
    content_description = models.TextField(max_length=1000, null=True, blank=True,
                                             help_text='Mô tả chi tiết, kiểu textarea')
    
  
    # logo cty
    # agt_logo = models.ImageField(upload_to='agent/images/', null=True, blank=True, help_text='Ảnh đại diện')

    # trạng thái
    content_enable = models.BooleanField(null=True,
                                           blank=True)  # , help_text='Trạng thái: True - Đang quản lý; False - Không còn quản lý'
    content_status = models.BooleanField(null=True, blank=True,
                                           default=True)  # , help_text='Trạng thái: True - đang hoạt động; False - đã xóa'
    
    content_local = models.ForeignKey('ContentLocal', related_name='Content_content_local',
                                               on_delete=models.SET_NULL, null=True, blank=True)

    content_user_created = models.ForeignKey(User, related_name='Content_content_user_created',
                                               on_delete=models.SET_NULL, null=True, blank=True)
    content_user_updated = models.ForeignKey(User, related_name='Content_content_user_updated',
                                               on_delete=models.SET_NULL, null=True, blank=True)

    # Thời gian tạo dữ liệu, tự động điền theo giờ hệ thống
    content_created_at = models.DateTimeField(auto_now_add=True)
    # Thời gian cập nhật - thay đổi dữ liệu, tự động điền theo giờ hệ thống
    content_updated_at = models.DateTimeField(auto_now=True)
    # img
    content_image = models.ImageField(upload_to='tinni/static',null=True,blank=True)
    # price
    content_price = models.FloatField(max_length=100,null=True,blank=True)
    def __str__(self):
        return self.content_name
    
    