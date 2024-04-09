from django.db import models


class MyBaseModel(models.Model):
    is_active = models.BooleanField(
        default=False,
        verbose_name='Is Active',
    )

    created_date = models.DateTimeField(
        null=True,
        auto_now_add=True,
        verbose_name='Created Date'
    )

    updated_date = models.DateTimeField(
        null=True,
        auto_now=True,
        verbose_name='Updated Date',
    )

    class Meta:
        abstract = True
        ordering = ('pk',)

    def __str__(self):
        raise NotImplementedError('Implement __str__ Method')


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


class Post(MyBaseModel):
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
    category = models.ForeignKey(Category,
                                 related_name='Posts',
                                 verbose_name='Category',
                                 on_delete=models.PROTECT,
                                 null=False,
                                 blank=False,
                                 )

    class Meta:
        verbose_name = 'Post'
        verbose_name_plural = 'Posts'
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
    post = models.ForeignKey(Post,
                             related_name='Comments',
                             verbose_name='Post',
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
    post = models.ForeignKey(Post,
                             related_name='Image',
                             verbose_name='Post',
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
    post = models.ForeignKey(Post,
                             related_name='Video',
                             verbose_name='Post',
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
