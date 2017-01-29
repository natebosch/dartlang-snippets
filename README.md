# UltiSnips snippets for Dart

A collection of snippets for writing Dart. Start by reading about [UltiSnips][]
if you haven't used if before.

[UltiSnips]: https://github.com/SirVer/ultisnips

# Highlights

Some of the snippets that save the most typing.

## Dart code

### `im`

Import line. `im<tab>some_package` becomes
`import 'package:some_package/some_package.dart';`

### `for`

For-in loop. `for<tab>element` becomes

```dart
for(var element in elements) {
  |
}
```

### `try`

Try-catch. Most useful from visual mode with a block selected, fills the
selection in the `try`, then tab to fill out the `catch`.

[![asciicast](https://asciinema.org/a/101189.png)](https://asciinema.org/a/101189)

### Methods

Each of these triggers has 2 modes. At the beginning of the line they generate a
top-level/instance method. After other characters they generate a closure.

- `m`
  - `m<tab>ReturnType<tab>methodName<tab>ArgType argument` becomes

     ```dart
     ReturnType methodName(ArgType argument) {
       |
     }
     ```
  -  After other characters: `m<tab>argument` becomes

     ```dart
     (argument) {
       |
     }
     ```
- `r`
  - `r<tab>ReturnType<tab>methodName<tab>ArgType argument` becomes

     `ReturnType methodName(ArgType argument) => |`
  -  After other characters: `r<tab>argument` becomes

     `(argument) => |`

Prepending either trigger with `a` makes it use 'async mode'. For example, at
the beginning of a line:

`ar<tab>ReturnType<tab>methodName<tab>ArgType argument` becomes

`Future<ReturnType> methodName(ArgType argument) async => |`

## Angular Snippets

### `co`

A `@Component` annotation and class. Saves the most time if you follow a naming
convention: a class name `SomeName` has a selector like `some-name`, a template
at `some_name.html`, and styles at `some_name.css` or `some_name.scss.css`.
Fills out a default name which works well if this component lives in a file
named `some_name.dart`.

[![asciicast](https://asciinema.org/a/101181.png)](https://asciinema.org/a/101181)

# Installation

Install this repository and UltiSnips using your favorite method. If you used
[vim-plug][]:

```vimscript
Plug 'SirVer/Ultisnips'
Plug 'natebosch/dartlang-snippets'
```
