import { HttpClient } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { Observable, of } from 'rxjs';
import { IChartValue, ICurrentValues, ILastValues } from '../interfaces';

const IS_MOCK: boolean = false;
const API_PATH: string = '/api';

@Injectable({
  providedIn: 'root'
})
export class ParseApiService {

  constructor(
    private http: HttpClient
  ) { }
  
  mockLastValues: IChartValue[] = [];

  getMockLastValues(amount: number): Observable<ILastValues> {
    const value = 24 + (Math.random() - 0.5) * 5;
    this.mockLastValues.push({ value: [new Date, value] });
    const mockData = this.mockLastValues.slice(-amount);
    return of({
      temperature: mockData,
      pressure: mockData,
      humidity: mockData
    });
  }

  getMockCurrent(): Observable<ICurrentValues> {
    const value = Math.round(24 + (Math.random() - 0.5) * 5);
    return of({
      temperature: value,
      pressure: value,
      humidity: value
    });
  }

  getCurrent(): Observable<ICurrentValues> {
    if (IS_MOCK) return this.getMockCurrent();
    return this.http.get<ICurrentValues>(API_PATH + '/current');
  }

  getLastValues(amount: number): Observable<ILastValues> {
    if (IS_MOCK) return this.getMockLastValues(amount);
    return this.http.get<ILastValues>(API_PATH + '/last-values', {
      headers: { amount: String(amount) }
    });
  }
}