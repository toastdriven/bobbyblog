from django.db import models
# from tastypie.resources import ModelResource
# from ckeditor.fields import RichTextField

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=200)
    category = models.ForeignKey('blog.Category')
    # body = models.TextField()
    body = models.TextField()
    # body_truncated = models.CharField(max_length=500, null=True, blank=True, editable=False)
    summary = models.TextField()

    def __unicode__(self):
        return self.title

    # def save(self, *args, **kwargs):
    #     self.body_truncated = self.title[:2]
    #     super(Post, self).save(*args, **kwargs) # Call the "real" save() method.


class Category(models.Model):
    title = models.CharField('title', max_length=250)
    slug = models.SlugField('slug', max_length=100, unique=True)
    parent = models.ForeignKey('self', blank=True, null=True, related_name='child')

    class Meta:
        verbose_name_plural = 'Categories'
        ordering = ['title']

    def __unicode__(self):
        p_list = self._recurse_for_parents(self)
        p_list.append(self.title)
        return self.get_separator().join(p_list)

    def _recurse_for_parents(self, cat_obj):
        p_list = []
        if cat_obj.parent_id:
            p = cat_obj.parent
            p_list.append(p.title)
            more = self._recurse_for_parents(p)
            p_list.extend(more)
        if cat_obj == self and p_list:
            p_list.reverse()
        return p_list

    def get_separator(self):
        return ' :: '

    def _parents_repr(self):
        p_list = self._recurse_for_parents(self)
        return self.get_separator().join(p_list)
    _parents_repr.short_description = 'Category parents'

    def save(self, *args, **kwargs):
        p_list = self._recurse_for_parents(self)
        # if self.title in p_list:
        #     raise validators.ValidationError('You must not save a category in itself')
        super(Category, self).save(*args, **kwargs)

    @models.permalink
    def get_absolute_url(self):
        return ('category_index', (), { 'category': self.slug })

# class Category(models.Model):
#     name = models.CharField(max_length=200)
#     slug = models.SlugField(max_length=200)
#     parent = models.ForeignKey('self', blank=True, null=True, related_name='child')
#     description = models.TextField(blank=True,help_text="Optional")

#     class Admin:
#             list_display = ('name', '_parents_repr')

#     def __str__(self):
#             p_list = self._recurse_for_parents(self)
#             p_list.append(self.name)
#             return self.get_separator().join(p_list)

#     def get_absolute_url(self):
#             if self.parent_id:
#                     return "/tag/%s/%s/" % (self.parent.slug, self.slug)
#             else:
#                     return "/tag/%s/" % (self.slug)

#     def _recurse_for_parents(self, cat_obj):
#             p_list = []
#             if cat_obj.parent_id:
#                     p = cat_obj.parent
#                     p_list.append(p.name)
#                     more = self._recurse_for_parents(p)
#                     p_list.extend(more)
#             if cat_obj == self and p_list:
#                     p_list.reverse()
#             return p_list

#     def get_separator(self):
#             return ' :: '

#     def _parents_repr(self):
#             p_list = self._recurse_for_parents(self)
#             return self.get_separator().join(p_list)
#     _parents_repr.short_description = "Tag parents"

#     def save(self):
#             p_list = self._recurse_for_parents(self)
#             if self.name in p_list:
#                     raise validators.ValidationError("You must not save a category in itself!")
#             super(Category, self).save()
