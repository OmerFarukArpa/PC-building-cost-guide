from django.db import models
from django.contrib.auth.models import User






# kategori
class Category(models.Model):
    name = models.CharField(max_length=255)
    image_url = models.CharField(max_length=255, null=True)
    description = models.CharField(max_length=255, null=True)

    
    def __str__(self):
        return self.name
    
# ürün
class Product(models.Model):
    name = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=7, decimal_places=2)
    image_url = models.CharField(max_length=255)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
    

class Sepet(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.user.username}'s Sepet"


class SepetItem(models.Model):
    sepet = models.ForeignKey(Sepet, related_name='items', on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return f"{self.quantity} x {self.product.name}"

    @property
    def total_price(self):
        return self.quantity * self.product.price
    

# anakart özellikleri
class MotherboardFeature(models.Model):
    processor_Socket_Type = models.CharField(max_length=255,null=True)
    ram_Type = models.CharField(max_length=255,null=True)
    compatible_Processors =models.CharField(max_length=255,null=True)
    motherboard_Size = models.CharField(max_length=255,null=True)
    
    product = models.OneToOneField(Product, on_delete=models.CASCADE, related_name='MotherboardFeature')

    def __str__(self):
        return f"{self.product, self.processor_Socket_Type, self.ram_Type, self.compatible_Processors, self.motherboard_Size}"


# bilgisayar kasası özellikleri  
class ComputerCaseFeature(models.Model):
    case_Type = models.CharField(max_length=255,null=True)
    PSU = models.CharField(max_length=255,null=True)
    PSU_Location = models.CharField(max_length=255,null=True)
    transparent_Case = models.CharField(max_length=255,null=True)
    type_C = models.CharField(max_length=255,null=True)

    product = models.OneToOneField(Product, on_delete=models.CASCADE, related_name='ComputerCaseFeature')

    def __str__(self):
        return f"{self.product}, {self.case_Type}, {self.PSU}, {self.PSU_Location}, {self.transparent_Case}, {self.type_C}"


# ekrankartı özellikleri
class GraphicsCardFeature(models.Model):
    gpu_Manufacturer = models.CharField(max_length=255,null=True)
    gpu_Model = models.CharField(max_length=255,null=True)
    memory_Type = models.CharField(max_length=255,null=True)
    gpu_Memory_Capacity = models.CharField(max_length=255,null=True)

    product = models.OneToOneField(Product, on_delete=models.CASCADE, related_name='GraphicsCardFeature')

    def __str__(self):
        return f"{self.product}, {self.gpu_Manufacturer}, {self.gpu_Model}, {self.memory_Type}, {self.gpu_Memory_Capacity}"


# işlemci özellikleri
class ProcessorFeature(models.Model):
    processor_Model = models.CharField(max_length=255,null=True)
    processor_Manufacturer = models.CharField(max_length=255,null=True)
    processor_Socket_Type = models.CharField(max_length=255,null=True)
    processor_Series = models.CharField(max_length=255,null=True)
    core_Count = models.CharField(max_length=255,null=True)

    product = models.OneToOneField(Product, on_delete=models.CASCADE, related_name='ProcessorFeature')

    def __str__(self):
        return f"{self.product}, {self.processor_Model}, {self.processor_Manufacturer}, {self.processor_Socket_Type}, {self.processor_Series}, {self.core_Count}"


# kasa fanları özellikleri
class CaseFanFeature(models.Model):
    cooling_Type = models.CharField(max_length=255,null=True)
    fan_Count = models.CharField(max_length=255,null=True)
    led_Type = models.CharField(max_length=255,null=True)
    power_Connector = models.CharField(max_length=255,null=True)
    rpm = models.CharField(max_length=255,null=True)

    product = models.OneToOneField(Product, on_delete=models.CASCADE, related_name='CaseFanFeature')

    def __str__(self):
        return f"{self.product}, {self.cooling_Type}, {self.fan_Count}, {self.led_Type}, {self.power_Connector}, {self.rpm}"


# klavye özellikleri
class KeyboardFeature(models.Model):
    connection_Type = models.CharField(max_length=255,null=True)
    mechanical = models.BooleanField(null=True)
    keyboard_Layout = models.CharField(max_length=255,null=True)
    wrist_Support = models.BooleanField(null=True)
    numpad = models.BooleanField(null=True)

    product = models.OneToOneField(Product, on_delete=models.CASCADE, related_name='KeyboardFeature')

    def __str__(self):
        return f"{self.product}, {self.connection_Type}, {self.mechanical}, {self.keyboard_Layout}, {self.wrist_Support}, {self.numpad}"


# monitör özellikleri
class MonitorFeature(models.Model):
    screen_Size = models.CharField(max_length=255,null=True)
    resolution = models.CharField(max_length=255,null=True)
    refresh_Rate = models.CharField(max_length=255,null=True)
    panel_Type = models.CharField(max_length=255,null=True)
    response_Time = models.CharField(max_length=255,null=True)

    product = models.OneToOneField(Product, on_delete=models.CASCADE, related_name='MonitorFeature')

    def __str__(self):
        return f"{self.product}, {self.screen_Size}, {self.resolution}, {self.refresh_Rate}, {self.panel_Type}, {self.response_Time}"


# fare özellikleri
class MouseFeature(models.Model):
    connection_Type = models.CharField(max_length=255,null=True)
    tracking_Type = models.CharField(max_length=255,null=True)
    button_Count = models.CharField(max_length=255,null=True)
    usage_Type = models.CharField(max_length=255,null=True)
    max_DPI = models.CharField(max_length=255,null=True)

    product = models.OneToOneField(Product, on_delete=models.CASCADE, related_name='MouseFeature')

    def __str__(self):
        return f"{self.product}, {self.connection_Type}, {self.tracking_Type}, {self.button_Count}, {self.usage_Type}, {self.max_DPI}"


# ram özellikleri
class RamFeature(models.Model):
    ram_Type = models.CharField(max_length=255,null=True)
    ram_Capacity = models.CharField(max_length=255,null=True)
    ram_Frequency = models.CharField(max_length=255,null=True)
    channel_Type = models.CharField(max_length=255,null=True)
    ram_Compatibility = models.CharField(max_length=255,null=True)

    product = models.OneToOneField(Product, on_delete=models.CASCADE, related_name='RamFeature')

    def __str__(self):
        return f"{self.product}, {self.ram_Type}, {self.ram_Capacity}, {self.ram_Frequency}, {self.channel_Type}, {self.ram_Compatibility}"


# soğutucular özellikleri
class CoolerFeature(models.Model):
    compatible_Sockets = models.CharField(max_length=255,null=True)
    cooling_Type = models.CharField(max_length=255,null=True)
    led = models.CharField(max_length=255,null=True)
    radiator_Size = models.CharField(max_length=255,null=True)
    fan_Count = models.IntegerField(null=True)

    product = models.OneToOneField(Product, on_delete=models.CASCADE, related_name='CoolerFeature')

    def __str__(self):
        return f"{self.product}, {self.compatible_Sockets}, {self.led}, {self.radiator_Size}, {self.fan_Count}"
