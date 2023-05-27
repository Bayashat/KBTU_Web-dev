import { HttpClient } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { Observable } from 'rxjs';
import { Post, Comment } from './models';

@Injectable({  // Injectable decorator means that this service can be injected into other components
  providedIn: 'root'  // root means that this service is available for all components
})
export class PostService {
  BASE_URL: string;

  constructor(private client: HttpClient) {
    this.BASE_URL = "https://jsonplaceholder.typicode.com";
  }  // HttpClient is a service that allows us to make HTTP requests

  getPosts(): Observable<Post[]> {
    return this.client.get<Post[]>(`${this.BASE_URL}/posts`);
  }

  getPost(id: number): Observable<Post> {
    return this.client.get<Post>(`${this.BASE_URL}/posts/${id}`);
  }

  addPost(post: Post): Observable<Post> {
    return this.client.post<Post>(`${this.BASE_URL}/posts`, post);
  }

  updatePost(post: Post): Observable<Post> {
    return this.client.put<Post>(`${this.BASE_URL}/posts/${post.id}`, post);
  }

  deletePost(id:number): Observable<any> {
    return this.client.delete<any>(`${this.BASE_URL}/posts/${id}`);
  }

  getPostComments(id: number): Observable<Comment[]> {
    return this.client.get<Comment[]>(`${this.BASE_URL}/posts/${id}/comments`)
  }

}
