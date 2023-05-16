reviewer: 윤금재
---
- related_name이 무엇인가요?
```
class Blog(models.Model):
  ...
 author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='blogs') 
```
related_name은 역방향 관계에서 사용할 이름을 지정한 것입니다.
(기본적으로 '모델명_set'으로 역방향 참조가 가능한데, 이것을 커스텀 한 것)

- null=True, blank=True는 무엇인가요?
```
class Post(models.Model):
  ...
  category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True) #카테고리
```
null=True: 이 옵션이 설정되면, 해당 필드는 데이터베이스에 NULL 값을 가질 수 있습니다. 즉, 이 필드는 데이터베이스 상에서 비어 있을 수 있다는 것을 의미합니다.

blank=True: 이 옵션이 설정되면, 해당 필드는 폼 검증(form validation)에서 빈 값('')이 될 수 있습니다. 즉, 사용자가 이 필드를 입력하지 않아도, 폼 검증에서 에러가 발생하지 않습니다.

위와 같이 설정함으로써, post는 category를 꼭 가지지 않아도 됩니다.

- PostTag의 __str__은 꼭 있어야 하는건가요?
```
class PostTag(models.Model): #Post와 Tag의 ManyToMany관계를 피하기 위해 사용한 중간모델 
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    tag = models.ForeignKey(Tag, on_delete=models.CASCADE)
     
    def __str__(self):
        return f"{self.post.title} - {self.tag.name}"

```
위의 PostTag 모델에서 __str__ 메소드는 해당 PostTag 객체가 어떤 Post와 Tag에 연결되어 있는지를 표현하는 문자열을 반환합니다. 
이렇게 하면 PostTag 객체를 보았을 때, 그것이 어떤 게시물과 태그 사이의 관계를 나타내는지 쉽게 이해할 수 있습니다.

따라서, 이 __str__ 메소드는 PostTag 객체의 정보를 더 명확하게 이해하는 데 도움이 됩니다. 
이 메소드가 없다면, PostTag 객체는 대개 그냥 메모리 주소나 기타 유용하지 않은 정보만을 표시하게 됩니다.

---
## 수정(추가)하는것도 좋을 것 같아요
1. 블로그별로 카테고리가 다르므로, 카테고리 클래스는 Blog를 ForeignKey로 가지면 좋겠어요
```
class Category(models.Model):
    name = models.CharField(max_length=200) #카테고리명
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE)
    def __str__(self):
        return self.name
```
2. 게시물의 생성시각, 수정시각 등을 따로 저장하는 것도 좋을 것 같아요
3. 게시물 추천 수 등을 저장하는것도 좋을 것 같아요
