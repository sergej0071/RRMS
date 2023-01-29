import { of } from "rxjs";
import { IApiValues, IChartValues, ICurrentValues } from "../interfaces";
import { ParseApiService } from "./parse-api.service";

describe('ParseApiService', () => {

  it('should return similar obj by getCurrent', () => {
    const testObj: ICurrentValues = {
      temperature: 23,
      pressure: 22,
      humidity: 22
    }

    const spy = jasmine.createSpyObj('HttpClient', { get: of(testObj) });
    const parseApiService: ParseApiService = new ParseApiService(spy);

    parseApiService.getCurrent().subscribe((value) => {
      expect(value).toEqual(testObj);
    }).unsubscribe();
  });

  it('should modify object correctly', () => {
    const inputObj: IApiValues = {
      realData: [
        {
          temperature: 12,
          pressure: 23,
          humidity: 34,
          date: new Date(123)
        }
      ],
      prognosisData: [
        {
          temperature: 45,
          pressure: 56,
          humidity: 67,
          date: new Date(1234)
        }
      ]
    };

    const outputObj: IChartValues = {
      realData: {
        temperature: [{ value: [new Date(123), 12] }],
        pressure: [{ value: [new Date(123), 23] }],
        humidity: [{ value: [new Date(123), 34] }],
      },
      prognosisData: {
        temperature: [{ value: [new Date(1234), 45] }],
        pressure: [{ value: [new Date(1234), 56] }],
        humidity: [{ value: [new Date(1234), 67] }],
      }
    };

    const spy = jasmine.createSpyObj('HttpClient', { get: of(inputObj) });
    const parseApiService: ParseApiService = new ParseApiService(spy);

    parseApiService.getLastValues(1).subscribe((value) => {
      expect(value).toEqual(outputObj);
    }).unsubscribe();
  });


});