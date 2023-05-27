#   Week-6
## Modules, Router Module
## Getting Data From RESTful APIs

* Reactive Programming
* Services
* Observables

## Laboratory Work - 6: https://docs.google.com/document/d/114Wr4YzCYYtrNSrjApFQ2MJXCHdRTTvJCVLAlHstt8I/edit?usp=sharing


##  What I did: 
### 1. Create project and components
```bash
1. 使用 "ng new demo" 创建了此项目
2. 使用 "ng g c home/about/not-found/posts/post-detail" 创建了 components
```
### 2. Configure Routes
```bash
1. 在 app-routing.module.ts 文件里配置了各个路由，并且配置了"空"URL和"其他"URL的情况
2. 在 app.component.html, 将上方(header)作为根据点击时跳转路由的导航区域. 并在下面放置 <router-outlet></router-outlet> 以根据URL来变化的区域
```
### 3. Create Models and Local Database
```bash
1. 在models.ts 和 fake-db.ts 文件里创建了Post interface 和 本地数据库 POSTS
```

### 4. Displaying Data for Posts
```bash
1. 当点击posts时, 我们需要看见目前所有的posts. 为此我们在post组件下的ts文件里, 在 ngOninit 函数里导入数据库中的POSTS
2. 当我们点击某个具体的post时, 我们需要跳转至此post的详细页面. 为此我们有 post-detail 组件 和 posts/:id URL
3. 在post-detail里的ts文件里,我们在ngOninit函数里通过 ActivatedRoute的snapshot 或者 paramMap.subscribe 来获取URL里的id
4. 得到id后, 我们从本地数据库里查找到对应的Post, 并且显示在HTML页面里
```

### 5. Creating a Service(Observable): Service 是用来通过其他Resource获取并处理数据的
```bash
1. 通过 "ng g service post" 创建了 post.service.ts 文件. 在里面我们可以看见 @Injectable, 这代表用它decorate的class在所有的组件都可以用
2. 为了从Angular发送HTTP请求, 我们需要导入 HttpClient 和 Observable(在 app.module.ts 里导入 HttpClientModule from '@angular/common/http'), 并且创建一个postService的class
4. 在 post.service.ts 文件里, 我们需要在constructor里用 private http: HttpClient 来创建一个http的实例, 用来发送HTTP请求
```

### 6. CRUD Operations: Create, Read, Update, Delete

####    1) Getting Data From RESTful APIs (Get Posts): 
0. Web-Site URL: https://jsonplaceholder.typicode.com/guide/
1. 我们需要发送get请求以从网站得到Posts的数据
2. 在 service 里的getPosts()函数里, 我们需要用 http.get('URL') 来发送get请求, 并且返回一个Observable<Post[]>
3. 在 post.component.ts 里的ngOninit函数里, 我们需要用 postService.getPosts().subscribe(posts => this.posts = posts) 来获取posts. 这时我们可以看到网站上的所有posts了
4. 现在我们需要在点击某个Post时,显示该Post的具体信息. 为此我们需要在 post.service.ts 文件里创建getPost(id)函数, 用来从数据库获取某个id的post. 并 在 post-detail.component。ts 里的ngOninit函数里, 我们需要用 postService.getPost(id).subscribe(post => this.post = post) 来获取post. 这时我们可以看到网站上的某个post的详细信息了

####    2) Creating Data (Create Post)
1. 现在我们需要在网站上创建一个post
2. 为此在 post.service.ts 文件里创建 addPost(post) 函数, 并且用 http.post('URL', post) 来发送post请求
3. 在 html 文件里创建一个表单, 并且用 ngModel 来绑定表单里的数据. 
4. 在 post.component.ts 文件里创建 addPost()函数, 我们用 postService.addPost(post).subscribe(post => this.posts.unshift(post)) 来创建一个post, 并且将其添加到posts的最前面
5. 注意: 创建的Post只会在本地数据库里创建, 并不会在网站上创建. 每次刷新网站, 该post都会消失

####    3-Updating Data (Update Post)
1. 现在我们需要在网站上更新一个post
2. 为此在 post.service.ts 文件里创建 updatePost(post) 函数, 用来更新一个post. 并且用 http.put('URL', post) 来发送put请求
3. 在 html 文件里创建一个表单, 并且用 ngModel 来绑定表单里的数据.
4. 在 post.component.ts 文件里创建 updatePost()函数, 我们用 postService.updatePost(post).subscribe(post => {}) 来更新一个post为表单里更改的post
5. 注意: 更新的Post只会在本地数据库里更新, 并不会在网站上更新. 每次刷新网站, 该post都会恢复到原来的状态

####    4-Deleting Data (Delete Post)
1. 现在我们需要在网站上删除一个post
2. 为此在 post.service.ts 文件里创建 deletePost(post) 函数, 用来删除一个post. 并且用 http.delete('URL') 来发送delete请求
3. 在 post.component.ts 文件里创建 deletePost()函数, 我们用 postService.deletePost(this.post);
4. 注意: 删除的Post只会在本地数据库里删除, 并不会在网站上删除. 每次刷新网站, 该post都会恢复到原来的状态

####    5-Show Comments
1. 现在我们需要在网站上显示某个post的comments
2. 为此在 post.service.ts 文件里创建 getPostComments(id) 函数, 用来获取某个post的comments. 并且用 http.get('URL') 来发送get请求
3. 在 post-detail.component.ts 文件里的showComments函数里, 我们用 postService.getPostComments(this.post.id).subscribe(comments => this.comments = comments) 来获取comments
4. 当点击showComments时, 我们需要显示comments, 为此我们在 post-detail.component.html 文件里创建一个div, 并且用 ngFor 来遍历comments, 并且显示在网页上
