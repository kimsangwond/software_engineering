export default function isPasswordSame(form) {
    let password1 = form.pw
    let password2 = form.pw2
    if (password1 == password2) {
        return true
    } else {
        return false
    }
}

