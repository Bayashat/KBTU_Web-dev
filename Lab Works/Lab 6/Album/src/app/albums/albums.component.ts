import { Component, OnInit } from '@angular/core';
import { Album } from '../models'
import { AlbumService } from '../album.service';
import { ALBUMS } from '../fake-db';

@Component({
  selector: 'app-albums',
  templateUrl: './albums.component.html',
  styleUrls: ['./albums.component.css']
})
export class AlbumsComponent implements OnInit{
  albums: Album[];
  loaded: boolean;
  newAlbum: Album;

  constructor(private albumService: AlbumService){
    this.albums = [];
    this.loaded = true;
    this.newAlbum = {} as Album;
  }

  ngOnInit(): void {
    this.getAlbums();
  }

  getAlbums(){  
    // working with local db
    // this.albums = ALBUMS;

    this.loaded = false;
    this.albumService.getAlbums().subscribe((albums) => {
      this.albums = albums;
      this.loaded = true;
    });
  }

  deleteAlbum(id: number){
    this.albums = this.albums.filter((x) => x.id !== id);
    this.albumService.deleteAlbum(id).subscribe(() => {
      console.log('deleted', id);
      
  }); 
  }

  addAlbum(){ 
    this.loaded = false;
    this.albumService.addAlbum(this.newAlbum).subscribe((album) => {
        this.albums.push(album);
        this.loaded = true;
        this.newAlbum = {} as Album;
    });
  }

}

