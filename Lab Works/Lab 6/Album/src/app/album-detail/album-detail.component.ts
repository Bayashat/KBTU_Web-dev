import { Component, OnInit } from '@angular/core';
import { ActivatedRoute } from '@angular/router';
import { ALBUMS } from '../fake-db';
import { Album, Photo } from '../models';
import { Location } from '@angular/common';
import { AlbumService } from '../album.service';

@Component({
  selector: 'app-album-detail',
  templateUrl: './album-detail.component.html',
  styleUrls: ['./album-detail.component.css']
})
export class AlbumDetailComponent implements OnInit {
  album: Album;
  is_edit: boolean;

  constructor(private route: ActivatedRoute,
              private location: Location,
              private albumService: AlbumService) {
    this.album = {} as Album;
    this.is_edit = false;
  }

  ngOnInit(): void {
    // working with local db
    this.getAlbum();
  }

  getAlbum(){
    this.route.paramMap.subscribe((params) => {
      const id = Number(params.get('id'));
      // this.album = ALBUMS.find((x) => x.id === id) as Album;
      this.albumService.getAlbum(id).subscribe((album) => {
        this.album = album as Album;
      });
      });
  }

  goBack(){
    this.location.back()
  }

  updateAlbum(){
    this.albumService.updateAlbum(this.album).subscribe((album) => {
      console.log(album);
      this.is_edit = false;
    })
  }

  editAlbum(){
    this.is_edit = true;
  }


}
