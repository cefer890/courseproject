from django.db import models

# Create your models here.
class Blog(models.Model):
    title = models.CharField("Basliq", max_length=250)
    desc = models.TextField("Metini daxil edin")
    status = models.BooleanField("Status", default=True)
    view_count = models.PositiveIntegerField('Baxis sayi', default=0)
    images = models.ImageField("Sekil", upload_to='blog', null=True, blank=True)


    def __str__(self):
        return self.title

    class Meta:
        verbose_name="Blog"
        verbose_name_plural = "Blogs"



class News(models.Model):
    title = models.CharField("Title",max_length=250)
    desc = models.TextField("Metini daxil edin")
    status = models.BooleanField("Status", default=True)
    view_count = models.PositiveIntegerField("Baxis sayi", default=0)
    cover = models.ImageField("Cover Image", upload_to="news", null=True, blank=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updata_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name="News"
        verbose_name_plural = "Newss"

class Xiomi(models.Model):
    title = models.CharField("Model",max_length=250)
    desc = models.TextField("Xususiyyetler")
    des = models.TextField("1")
    de = models.TextField("2")
    d = models.TextField("3")
    price = models.DecimalField("Price", max_digits=12, decimal_places=2)
    view_count = models.PositiveIntegerField("Baxis sayi", default=0)
    cover = models.ImageField("Cover Image", upload_to="xiomi", null=True, blank=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updata_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name="Xiomi"
        verbose_name_plural = "Xiomis"


class PhoneCategory(models.Model):
    name = models.CharField('Name', max_length=100)

    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)


    def __str__(self):
        return self.name


class PhoneColor(models.Model):
    name = models.CharField('Name', max_length=100)

    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)


    def __str__(self):
        return self.name

PHONE_TYPE = ((1,"32GB"), (2,"64GB"))

class Phone(models.Model):
    fk = models.ForeignKey(PhoneCategory, related_name='phone_category', on_delete=models.CASCADE)
    title = models.CharField("Basliq", max_length=250)
    type = models.PositiveIntegerField('yaddas', choices=PHONE_TYPE, default=1)
    desc = models.TextField("Metni daxil edin")
    upc = models.CharField("UPC", max_length=15, unique=True)
    color = models.ManyToManyField(PhoneColor, related_name='phone_color', blank=True)

    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

class ProductsAttribute(models.Model):
    name = models.CharField("name",max_length=100)

    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class ProductsClass(models.Model):
    name = models.CharField("name", max_length=100)

    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

class Products(models.Model):
    fk = models.ForeignKey(ProductsAttribute, related_name='products_attribute', on_delete=models.CASCADE)
    title = models.CharField("Basliq",max_length=250)
    desc = models.TextField("Metni daxil edin")
    upc = models.CharField("UPC", max_length=15, unique=True)
    sinif = models.ManyToManyField(ProductsClass, related_name='products_class', blank=True)
    # files = models.FileField('File', upload_to='files')

    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name="Products"
        verbose_name_plural = "Productss"

class Users(models.Model):
    first_name = models.CharField("firs name" ,max_length=25)
    last_name = models.CharField("last name" ,max_length=30)
    email =  models.EmailField("email",unique=True)
    birth_date = models.DateField("birth date")

    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return "{} {}".format(self.last_name ,self.first_name)

    class Meta:
        verbose_name="Users"
        verbose_name_plural = "Userss"

class Sides(models.Model):
    title = models.CharField("Basliq", max_length=250)
    desc = models.TextField("Metni daxil edin")
    image = models.ImageField("Image", upload_to="sides", null=True, blank=True)
    status = models.BooleanField("Status", default=True)
    url = models.URLField("URL", max_length=50)
    contact_email =  models.EmailField("email",unique=True)

    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name="sides"
        verbose_name_plural = "sidess"



