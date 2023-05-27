import {
    HttpErrorResponse,
    HttpEvent,
    HttpHandler,
    HttpInterceptor,
    HttpRequest,
    HttpResponse
} from "@angular/common/http";
import {Injectable} from "@angular/core";
import {Observable, tap} from "rxjs";


@Injectable()
export class AuthInterceptor implements HttpInterceptor {
    constructor() {}

    intercept(req: HttpRequest<any>, next: HttpHandler): Observable<HttpEvent<any>> {
        const token = localStorage.getItem('token');
        if (token) {
            const newReq = req.clone({
                headers: req.headers.set('Authorization', `JWT ${token}`),  // add JWT token to header
            });
            return next.handle(newReq);
        }
        return next.handle(req);
    }
}
