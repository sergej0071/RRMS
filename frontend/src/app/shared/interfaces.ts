import { EChartsOption } from "echarts";

export interface IArticle {
  header: string;
  content: string;
}

export interface IChartValue {
  value: [Date, number]
}

export interface IArrayData {
  temperature: IChartValue[];
  pressure: IChartValue[];
  humidity: IChartValue[];
}

export interface IChartValues {
  realData: IArrayData;
  prognosisData: IArrayData;
}

export interface ICurrentValues {
  temperature: number;
  pressure: number;
  humidity: number;
}

export interface IApiValues {
  realData: IApiValue[];
  prognosisData: IApiValue[];
}

export interface IApiValue {
  temperature: number;
  pressure: number;
  humidity: number;
  date: Date;
}

export interface IPackageEChartOption {
  temperature: EChartsOption,
  pressure: EChartsOption,
  humidity: EChartsOption
}
