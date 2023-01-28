import { IArticle } from "./interfaces";

export const ARTICLES: IArticle[] = [
  {
    header: 'Page: Current',
    content: 'On this page we can observe the current state of the sensors. We get this data from the BMP280 sensor, which is attached to the Arduino Mega.'
  },
  {
    header: 'Page: Statistic',
    content: 'On this page we can observe graphs of changes of each sensor. You can select the time range for which the graph will be built.'
  }
];
