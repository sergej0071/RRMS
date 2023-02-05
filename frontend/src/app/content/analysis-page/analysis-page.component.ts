import { ChangeDetectionStrategy, Component, OnInit } from '@angular/core';
import { FormControl } from '@angular/forms';
import { EChartsOption } from 'echarts';
import { map, Observable } from 'rxjs';
import { ICorrelationApi, IPackageEChartOption, IPackageEChartOptionCorrelation, IProbabilityApi } from 'src/app/shared/interfaces';
import { ParseApiService } from 'src/app/shared/services/parse-api.service';
import { MAX_VALUE, MIN_VALUE } from 'src/app/shared/setup-charts';

@Component({
  selector: 'app-analysis-page',
  templateUrl: './analysis-page.component.html',
  styleUrls: ['./analysis-page.component.scss'],
  changeDetection: ChangeDetectionStrategy.OnPush
})
export class AnalysisPageComponent implements OnInit {

  public probability$!: Observable<IPackageEChartOption>;
  public correlation$!: Observable<IPackageEChartOptionCorrelation>;

  public valueControl: FormControl<number | null> = new FormControl<number>(MIN_VALUE);

  public minValue: number = MIN_VALUE;
  public maxValue: number = MAX_VALUE;

  public cutting(value: number){
    return Math.round(value * 10000)/10000;
  }

  constructor(
    public parseApiService: ParseApiService
  ) { }

  public ngOnInit(): void {
    this.reloadData()
  }

  public reloadData() {
    this.probability$ = this.parseApiService.getProbability(this.valueControl.value!).pipe(
      map((value: IProbabilityApi) => ({
        temperature: this.setChart(value.temperature.value, value.temperature.amount, 'bar', 'Temp', 'Amount'),
        pressure: this.setChart(value.pressure.value, value.pressure.amount, 'bar', 'Pressure', 'Amount'),
        humidity: this.setChart(value.humidity.value, value.humidity.amount, 'bar', 'Humidity', 'Amount')
      })));

    this.correlation$ = this.parseApiService.getCorrelation(this.valueControl.value!).pipe(
      map((value: ICorrelationApi) => ({
        temperaturePressureChart: this.setChart(value.data.temperature, value.data.pressure, 'scatter', 'Temperature', 'Pressure'),
        temperatureHumidityChart: this.setChart(value.data.temperature, value.data.humidity, 'scatter', 'Temperature', 'Humidity'),
        pressureHumidityChart: this.setChart(value.data.pressure, value.data.humidity, 'scatter', 'Pressure', 'Humidity'),
        temperaturePressure: this.cutting(value.coefCorrelation.temperaturePressure),
        temperatureHumidity: this.cutting(value.coefCorrelation.temperatureHumidity),
        pressureHumidity: this.cutting(value.coefCorrelation.pressureHumidity)
      })));
  }

  private setChart(dataFirst: number[], dataSecond: number[], type: 'bar' | 'scatter', xName: string, yName: string): EChartsOption {
    return {
      color: ['#F4D800'],
      tooltip: {},
      xAxis: {
        name: xName,
        data: dataFirst,
        silent: false,
        splitLine: { show: false, },
      },
      yAxis: { name: yName },
      series: [{
        type,
        data: dataSecond,
        animationDelay: (idx) => idx * 10,
      }],
      animationEasing: 'elasticOut',
    };
  }

}
