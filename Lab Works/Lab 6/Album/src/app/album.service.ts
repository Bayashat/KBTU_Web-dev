import { HttpClient } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { ALBUMS } from './fake-db';
import { Observable, of } from 'rxjs'
import { Album, Photo } from './models';

@Injectable({
  providedIn: 'root'
})
export class AlbumService {

  BASE_URL: string = 'https://jsonplaceholder.typicode.com';
  constructor(private client: HttpClient) { }

  //        1. working with local db
  // getAlbums(){
  //   return of(ALBUMS);
  // }

  // getAlbum(id: number){
  //   const album = ALBUMS.find((album) => album.id === id);
  //   return of(album);
  // }

  //      2. working with http client 
  getAlbums(): Observable<Album[]> {
    return this.client.get<Album[]>(`${this.BASE_URL}/albums`)
  }

  getAlbum(id: number): Observable<Album>{
    return this.client.get<Album>(`${this.BASE_URL}/albums/${id}`)
  }

  getPhoto(id: number): Observable<Photo[]>{
    return this.client.get<Photo[]>(`${this.BASE_URL}/albums/${id}/photos`)
  }

  deleteAlbum(id: number): Observable<any> {
    return this.client.delete(`${this.BASE_URL}/albums/${id}`)
  }

  updateAlbum(album: Album): Observable<Album> {
    return this.client.put<Album>(`${this.BASE_URL}/albums/${album.id}`, album)
  }

  addAlbum(album: Album): Observable<Album> {
    return this.client.post<Album>(`${this.BASE_URL}/albums`, album)
  }
  

}