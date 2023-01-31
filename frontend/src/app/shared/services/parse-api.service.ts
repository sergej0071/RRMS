import { HttpClient } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { map, Observable, of } from 'rxjs';
import { IArrayData, IChartValue, IChartValues, ICurrentValues, IApiValues, IApiValue } from '../interfaces';

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

  getMockLastValues(amount: number): Observable<IChartValues> {
    const value = 24 + (Math.random() - 0.5) * 5;
    this.mockLastValues.push({ value: [new Date(), value] });
    const mockData = this.mockLastValues.slice(-amount);
    return of({
      realData: {
        temperature: mockData,
        pressure: mockData,
        humidity: mockData
      },
      prognosisData: {
        temperature: [],
        pressure: [],
        humidity: []
      }
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

  getLastValues(amount: number): Observable<IChartValues> {
    if (IS_MOCK) return this.getMockLastValues(amount);
    const reduceFunc = (prev: IArrayData, current: IApiValue) => {
      prev.temperature.push({ value: [current.timeData, current.temperature] });
      prev.pressure.push({ value: [current.timeData, current.pressure] });
      prev.humidity.push({ value: [current.timeData, current.humidity] });
      return prev;
    };

    return this.http.get<IApiValues>(`${API_PATH}/last-values?amount=${amount}`).pipe(
      map((statisticValues: IApiValues) => ({
        realData: {
          ...statisticValues.realData.reduce(reduceFunc, {
            temperature: [],
            pressure: [],
            humidity: []
          })
        },
        prognosisData: {
          ...statisticValues.prognosisData.reduce(reduceFunc, {
            temperature: [],
            pressure: [],
            humidity: []
          })
        }
      }))
    );
  }
}
