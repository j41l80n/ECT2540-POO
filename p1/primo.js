function primo(numero) {
  for (var i = 2; i < numero/2; i++) {
    if (numero % i == 0) {
      console.log('primo')
    }
  }
  console.log('nao primo')
}