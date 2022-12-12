# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models

class TbCity(models.Model):
    city = models.CharField(max_length=50, blank=True, null=True)
    provinces = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tb_city'


class TbCustomer(models.Model):
    customer_id = models.AutoField(db_column='Customer_ID', primary_key=True)  # Field name made lowercase.
    customer_email = models.CharField(db_column='Customer_Email', max_length=100, blank=True, null=True)  # Field name made lowercase.
    customer_password = models.CharField(db_column='Customer_Password', max_length=50, blank=True, null=True)  # Field name made lowercase.
    customer_firstname = models.CharField(db_column='Customer_FirstName', max_length=100, blank=True, null=True)  # Field name made lowercase.
    customer_lastname = models.CharField(db_column='Customer_LastName', max_length=100, blank=True, null=True)  # Field name made lowercase.
    customer_contactnumber = models.CharField(db_column='Customer_ContactNumber', max_length=100, blank=True, null=True)  # Field name made lowercase.
    customer_dob = models.DateField(db_column='Customer_DOB', blank=True, null=True)  # Field name made lowercase.
    customer_shippingaddress = models.CharField(db_column='Customer_ShippingAddress', max_length=100, blank=True, null=True)  # Field name made lowercase.
    customer_city = models.CharField(db_column='Customer_City', max_length=100, blank=True, null=True)  # Field name made lowercase.
    customer_country = models.CharField(db_column='Customer_Country', max_length=100, blank=True, null=True)  # Field name made lowercase.
    customer_status = models.IntegerField(db_column='Customer_Status', blank=True, null=True)  # Field name made lowercase.
    order_map_lat = models.CharField(db_column='Order_Map_Lat', max_length=45, blank=True, null=True)  # Field name made lowercase.
    order_map_lon = models.CharField(db_column='Order_Map_Lon', max_length=45, blank=True, null=True)  # Field name made lowercase.
    class Meta:
        managed = False
        db_table = 'tb_customer'


class TbEmployees(models.Model):
    employee_id = models.AutoField(db_column='Employee_ID', primary_key=True)  # Field name made lowercase.
    employee_firstname = models.CharField(db_column='Employee_FirstName', max_length=100, blank=True, null=True)  # Field name made lowercase.
    employee_lastname = models.CharField(db_column='Employee_LastName', max_length=100, blank=True, null=True)  # Field name made lowercase.
    employee_title = models.CharField(db_column='Employee_Title', max_length=100, blank=True, null=True)  # Field name made lowercase.
    employee_gender = models.CharField(db_column='Employee_Gender', max_length=25, blank=True, null=True)  # Field name made lowercase.
    employee_dob = models.DateField(db_column='Employee_DOB', blank=True, null=True)  # Field name made lowercase.
    employee_hiredate = models.DateField(db_column='Employee_HireDate', blank=True, null=True)  # Field name made lowercase.
    employee_dept = models.CharField(db_column='Employee_Dept', max_length=25, blank=True, null=True)  # Field name made lowercase.
    employee_status = models.IntegerField(db_column='Employee_Status', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tb_employees'


class TbGuzeladmin(models.Model):
    username = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    role = models.CharField(db_column='Role', max_length=15)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tb_guzeladmin'


class TbOrder(models.Model):
    order_id = models.AutoField(db_column='Order_ID', primary_key=True)  # Field name made lowercase.
    order_trackingid = models.CharField(db_column='Order_TrackingID', max_length=100)  # Field name made lowercase.
    order_customerid = models.CharField(db_column='Order_CustomerID', max_length=100, blank=True, null=True)  # Field name made lowercase.
    order_customeremail = models.CharField(db_column='Order_CustomerEmail', max_length=50, blank=True, null=True)  # Field name made lowercase.
    order_productid = models.CharField(db_column='Order_ProductID', max_length=100, blank=True, null=True)  # Field name made lowercase.
    order_productname = models.CharField(db_column='Order_ProductName', max_length=100, blank=True, null=True)  # Field name made lowercase.
    order_productsku = models.CharField(db_column='Order_ProductSKU', max_length=100, blank=True, null=True)  # Field name made lowercase.
    order_productprice = models.CharField(db_column='Order_ProductPrice', max_length=100, blank=True, null=True)  # Field name made lowercase.
    order_productqty = models.CharField(db_column='Order_ProductQty', max_length=100, blank=True, null=True)  # Field name made lowercase.
    order_productsubtotal = models.CharField(db_column='Order_ProductSubTotal', max_length=100, blank=True, null=True)  # Field name made lowercase.
    order_date = models.DateField(db_column='Order_Date')  # Field name made lowercase.
    order_isshipped = models.IntegerField(db_column='Order_isShipped')  # Field name made lowercase.
    order_map_lat = models.CharField(db_column='Order_Map_Lat', max_length=45, blank=True, null=True)  # Field name made lowercase.
    order_map_lon = models.CharField(db_column='Order_Map_Lon', max_length=45, blank=True, null=True)  # Field name made lowercase.
    class Meta:
        managed = False
        db_table = 'tb_order'


class TbProduct(models.Model):
    product_id = models.AutoField(db_column='Product_ID', primary_key=True)  # Field name made lowercase.
    product_category_id = models.IntegerField(db_column='Product_Category_ID', blank=True, null=True)  # Field name made lowercase.
    product_name = models.CharField(db_column='Product_Name', max_length=25, blank=True, null=True)  # Field name made lowercase.
    product_description = models.CharField(db_column='Product_Description', max_length=100, blank=True, null=True)  # Field name made lowercase.
    product_sku = models.CharField(db_column='Product_SKU', max_length=25, blank=True, null=True)  # Field name made lowercase.
    product_price = models.CharField(db_column='Product_Price', max_length=100, blank=True, null=True)  # Field name made lowercase.
    product_qty_instock = models.IntegerField(db_column='Product_Qty_InStock', blank=True, null=True)  # Field name made lowercase.
    product_image = models.CharField(db_column='Product_Image', max_length=100, blank=True, null=True)  # Field name made lowercase.
    productsupplier_id = models.CharField(db_column='ProductSupplier_ID', max_length=25, blank=True, null=True)  # Field name made lowercase.
    product_creationdate = models.DateField(db_column='Product_CreationDate', blank=True, null=True)  # Field name made lowercase.
    ispopular = models.IntegerField(db_column='isPopular', blank=True, null=True)  # Field name made lowercase.
    isnewstock = models.IntegerField(db_column='isNewStock', blank=True, null=True)  # Field name made lowercase.
    issale = models.IntegerField(db_column='isSale', blank=True, null=True)  # Field name made lowercase.
    product_status = models.IntegerField(db_column='Product_Status', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tb_product'


class TbProductCategory(models.Model):
    product_category_id = models.AutoField(db_column='Product_Category_ID', primary_key=True)  # Field name made lowercase.
    product_category_name = models.CharField(db_column='Product_Category_Name', max_length=25, blank=True, null=True)  # Field name made lowercase.
    product_category_status = models.IntegerField(db_column='Product_Category_Status', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tb_product_category'


class TbSupplier(models.Model):
    supplier_id = models.AutoField(db_column='Supplier_ID', primary_key=True)  # Field name made lowercase.
    supplier_name = models.CharField(db_column='Supplier_Name', max_length=100, blank=True, null=True)  # Field name made lowercase.
    supplier_businessname = models.CharField(db_column='Supplier_BusinessName', max_length=100, blank=True, null=True)  # Field name made lowercase.
    supplier_contactnumber = models.CharField(db_column='Supplier_ContactNumber', max_length=100, blank=True, null=True)  # Field name made lowercase.
    supplier_approvaldate = models.DateField(db_column='Supplier_ApprovalDate', blank=True, null=True)  # Field name made lowercase.
    supplier_city = models.CharField(db_column='Supplier_City', max_length=100, blank=True, null=True)  # Field name made lowercase.
    supplier_country = models.CharField(db_column='Supplier_Country', max_length=100, blank=True, null=True)  # Field name made lowercase.
    suppliertype_id = models.IntegerField(db_column='SupplierType_ID', blank=True, null=True)  # Field name made lowercase.
    supplier_status = models.IntegerField(db_column='Supplier_Status', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tb_supplier'


class TbSuppliertype(models.Model):
    suppliertype_id = models.AutoField(db_column='SupplierType_ID', primary_key=True)  # Field name made lowercase.
    suppliertype = models.CharField(db_column='SupplierType', max_length=100, blank=True, null=True)  # Field name made lowercase.
    suppliertype_desc = models.CharField(db_column='SupplierType_Desc', max_length=100, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tb_suppliertype'
