from django.contrib.auth.models import User
from django.db import models

class Tag(models.Model):
    name = models.CharField(max_length=200) #태그명

    def __str__(self):
        return self.name

class Category(models.Model):
    name = models.CharField(max_length=200) #카테고리명

    def __str__(self):
        return self.name

class Blog(models.Model): #블로그
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='blogs') #블로그장
    title = models.CharField(max_length=200) #블로그 타이틀
    description = models.TextField() #블로그 설명

    def __str__(self):
        return self.title

class Post(models.Model): #게시물
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE, related_name='posts') #게시물이 속한 블로그
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='posts') #작성자
    title = models.CharField(max_length=200) #타이틀
    body = models.TextField() #내용
    date = models.DateField(auto_now_add=True) #날짜
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True) #카테고리

    def __str__(self):
        return self.title

class Comment(models.Model): #댓글
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='comments') #작성자
    comment = models.TextField() #내용
    post = models.ForeignKey(Post, on_delete=models.CASCADE) #댓글이 속한 게시물 
    date = models.DateField(auto_now_add=True) #날짜

    def __str__(self):
        return self.comment

class PostTag(models.Model): #Post와 Tag의 ManyToMany관계를 피하기 위해 사용한 중간모델 
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    tag = models.ForeignKey(Tag, on_delete=models.CASCADE)
     
    def __str__(self):
        return f"{self.post.title} - {self.tag.name}"


# class FreePost(models.Model):
#     author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='free_posts')
#     title = models.CharField(max_length=200)
#     body = models.TextField()
#     date = models.DateField(auto_now_add=True)
#     category = models.ForeignKey('Category', on_delete=models.SET_NULL, null=True, blank=True)

#     def __str__(self):
#         return self.title

# class FreeComment(models.Model):
#     author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='free_comments')
#     comment = models.TextField()
#     post = models.ForeignKey(FreePost, on_delete=models.CASCADE)
#     date = models.DateField(auto_now_add=True)

#     def __str__(self):
#         return self.comment



# Adding Tag as a ManyToManyField in Post and FreePost
