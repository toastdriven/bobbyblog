from tastypie import fields
from tastypie.resources import ModelResource, ALL, ALL_WITH_RELATIONS
from blog.models import Post, Category


class CategoryResource(ModelResource):
    parent = fields.ForeignKey('self', 'parent', full=True, null=True)

    class Meta:
        queryset = Category.objects.all()
        resource_name = 'category'
        filtering = {
            'title': ALL,
        }


class PostResource(ModelResource):
    category = fields.ForeignKey(CategoryResource, 'category', full=True)

    class Meta:
        queryset = Post.objects.all()
        resource_name = 'post'
        filtering = {
            "category": ALL_WITH_RELATIONS,
        }
