import { HttpClient } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { Observable } from 'rxjs';
import { ICurrentValues, ILastValues } from '../interfaces';

@Injectable({
  providedIn: 'root'
})
export class ParseApiService {

  constructor(
    private http: HttpClient
  ) { }

  getCurrent(): Observable<ICurrentValues> {
    return this.http.get<ICurrentValues>('/api/current');
  }

  getLastValues(amount: number): Observable<ILastValues> {
    return this.http.get<ILastValues>('/api/last-values', {
      headers: { amount: String(amount) }
    });
  }
}