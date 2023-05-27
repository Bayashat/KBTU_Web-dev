import { Location } from '@angular/common';
import { Component, OnInit } from '@angular/core';
import { ActivatedRoute } from '@angular/router';
import { AlbumService } from '../album.service';
import { Album, Photo } from '../models';

@Component({
  selector: 'app-album-photos',
  templateUrl: './album-photos.component.html',
  styleUrls: ['./album-photos.component.css']
})
export class AlbumPhotosComponent implements OnInit{
  photos: Photo[];
  loaded: boolean;

  constructor(private route: ActivatedRoute,
              private location: Location,
              private albumService: AlbumService){
    this.photos = []
    this.loaded = true;
  }

  ngOnInit(): void {
    this.getPhoto();
  }

  getPhoto(){
    this.route.paramMap.subscribe((params) => {
      const id = Number(params.get('id'));
      this.loaded = false;
      this.albumService.getPhoto(id).subscribe((photos) => {
        this.photos = photos;
        console.log(photos);
        
        this.loaded = true;
      });
      });
  }

  goBack(){
    this.location.back()
  }
}
