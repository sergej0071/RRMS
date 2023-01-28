import { Injectable } from "@angular/core";
import { BehaviorSubject } from "rxjs";

@Injectable({
    providedIn: 'root'
})
export class SettingsService {

    private theme$: BehaviorSubject<string> = new BehaviorSubject('light');

    public switchTheme() {
        this.theme$.next(
            this.theme$.getValue() === 'light'
                ? 'dark' : 'light');
    }

    public getTheme(): BehaviorSubject<string> {
        return this.theme$;
    }
}
