from django.db import models
from django.contrib.auth.models import User

CARABAYAR_CHOICES = (
    ('1','Kontan'),
    ('2','Kredit'),
)

class Penjualan(models.Model):
    konsumen = models.ForeignKey('Konsumen')
    tanggal = models.DateField()
    nama = models.CharField(max_length=50)

    class Meta:
        db_table = u'penjualan'

class ItemPenjualan(models.Model):
    penjualan = models.ForeignKey(Penjualan)
    barang = models.ForeignKey('Barang', null=True, blank=True)
    nama = models.CharField(max_length=50)
    banyak = models.IntegerField()
    harga = models.DecimalField(max_digits=12, decimal_places=2)

    class Meta:
        db_table = u'itempenjualan'

class Barang(models.Model):
    nama = models.CharField(max_length=50)
    satuan = models.CharField(max_length=10)
    harga = models.DecimalField(max_digits=12, decimal_places=2)
    harga_beli = models.DecimalField(max_digits=12, decimal_places=2)
    cdate = models.DateTimeField(auto_now_add=True)
    mdate = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = u'barang'

class Pembayaran(models.Model):
    penjualan = models.ForeignKey(Penjualan, null=True)
    cara_bayar = models.CharField(max_length=1, choices=CARABAYAR_CHOICES)
    nilai = models.DecimalField(max_digits=12, decimal_places=2)


