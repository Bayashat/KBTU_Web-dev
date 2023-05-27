import {Component, OnInit} from '@angular/core';
import {Comment, Post} from "../models";
import {ActivatedRoute} from "@angular/router";
import {Location} from '@angular/common';
import {POSTS} from "../fake-db";
import {PostService} from "../post.service";

@Component({
  selector: 'app-post-detail',
  templateUrl: './post-detail.component.html',
  styleUrls: ['./post-detail.component.css']
})
export class PostDetailComponent implements OnInit{
  post: Post;
  loaded: boolean;
  is_edit: boolean;
  comments: Comment[];
  show_comment: boolean;
  constructor(private route: ActivatedRoute, private postService: PostService, private location: Location) {
    this.post = {} as Post;
    this.loaded = true;
    this.is_edit = false;
    this.comments = [];
    this.show_comment = false;
  }

  ngOnInit() {
  //   1-st option to get data from address bar: this.route.snapshot.paramMap.get('id')

  //  const id = this.route.snapshot.paramMap.get('id');
  //   we have 2 options to convert this string to number:
  //   1) use if and +
  //   if(id) {  // if "id" is not null or undefined, then convert use + sign
  //     let num_id = +id;
  //   }

    //  2) use Number()
    // const id = Number(this.route.snapshot.paramMap.get('id'));
    // this.post = POSTS.find((post) => post.id === id) as Post;

    //   2-nd option to get data from address bar: this.route.paramMap.subscribe()
    this.getPost();
  }

  getPost() {
    this.route.paramMap.subscribe((params) => {
      const id = Number(params.get('id'));
      // this.post = POSTS.find((post) => post.id === id) as Post;
      this.loaded = false;
      this.postService.getPost(id).subscribe((post) => {
        this.post = post;
        this.loaded = true;
      })
    })
  }

  editPost() {
    this.is_edit = !this.is_edit;
  }
  goBack() {
    this.location.back();
  }

  updatePost() {
    this.loaded = false;
    this.postService.updatePost(this.post).subscribe((post) => {
      this.is_edit = false;
      this.loaded = true;
    })
  }

  showComments() {
    this.show_comment = !this.show_comment;
    if (this.show_comment){
      this.postService.getPostComments(this.post.id).subscribe((comments) => {
        this.comments = comments;
      });
    }
    else {
      this.comments = [];
    }
  }

  deletePost() {
    this.loaded = false;
    this.postService.deletePost(this.post.id).subscribe(() => {
      this.loaded = true;
      this.goBack();
    })
  }


}
