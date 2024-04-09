from django.db import models
from blog.models import MyBaseModel


class Category(MyBaseModel):
    title = models.CharField(max_length=100,
                             null=False,
                             blank=False,
                             verbose_name='Title',
                             )
    description = models.TextField(max_length=255,
                                   null=False,
                                   blank=False,
                                   verbose_name='Description',
                                   )

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'
        ordering = ('id',)

    def __str__(self):
        return self.title


class Product(MyBaseModel):
    title = models.CharField(max_length=100,
                             null=False,
                             blank=False,
                             verbose_name='Product',
                             )
    description = models.TextField(max_length=255,
                                   null=False,
                                   blank=False,
                                   verbose_name='Description',
                                   )
    category = models.ForeignKey(Category,
                                 related_name='Product',
                                 verbose_name='Category',
                                 on_delete=models.PROTECT,
                                 null=False,
                                 blank=False,
                                 )
    price = models.PositiveIntegerField(default=0,
                                        null=False,
                                        blank=False,
                                        # TODO: add choices for available or not
                                        )

    class Meta:
        verbose_name = 'Product'
        verbose_name_plural = 'Product'
        ordering = ('id',)

    def __str__(self):
        return self.title


class Comment(MyBaseModel):
    title = models.CharField(max_length=100,
                             null=False,
                             blank=False,
                             verbose_name='Title',
                             )
    description = models.TextField(max_length=255,
                                   null=False,
                                   blank=False,
                                   verbose_name='Description',
                                   )
    product = models.ForeignKey(Product,
                                related_name='Comments',
                                verbose_name='Product',
                                on_delete=models.PROTECT,
                                null=False,
                                blank=False,
                                )

    class Meta:
        verbose_name = 'Comment'
        verbose_name_plural = 'Comments'
        ordering = ('id',)

    def __str__(self):
        return self.title


class Image(MyBaseModel):
    title = models.CharField(max_length=100,
                             null=False,
                             blank=False,
                             verbose_name='Title',
                             )
    product = models.ForeignKey(Product,
                                related_name='Image',
                                verbose_name='Product',
                                on_delete=models.PROTECT,
                                null=False,
                                blank=False,
                                )
    image = models.ImageField(upload_to="blog_images/")

    class Meta:
        verbose_name = 'Image'
        verbose_name_plural = 'Images'

    def __str__(self):
        return self.title


class Video(MyBaseModel):
    title = models.CharField(max_length=100,
                             null=False,
                             blank=False,
                             verbose_name='Title',
                             )
    product = models.ForeignKey(Product,
                                related_name='Video',
                                verbose_name='Product',
                                on_delete=models.PROTECT,
                                null=False,
                                blank=False,
                                )
    video = models.FileField(upload_to="blog_video/")

    class Meta:
        verbose_name = 'Video'
        verbose_name_plural = 'Videos'

    def __str__(self):
        return self.title
