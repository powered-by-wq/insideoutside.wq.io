# Inside/Outside project

We built the Inside/Outside Project for the Create Together Day at the 2017 Citizen Science Conference. The goal of the Inside/Outside Project is to train TensorFlow models that will classify whether any particular photo was taken inside or outside. The filtered dataset can then be provided to a second human-aided classification step; for example, to help build a repository of public places.
 
The Inside/Outside project involves three components:
 1. This repository, which contains the [wq-powered](https://wq.io) client application and observation database for collecting training images.
 2. The [TensorFlow+wq](https://tensorflow.wq.io) model broker database, which passes the classified training images on to the retrainer
 3. The [CitSci2017 TensorflowRetrainer](https://github.com/marco-willi/CitSci2017_TensorflowRetrainer), which retrains Inception on the training data and uploads the resulting model back to the broker.

## Implementation Details
This application was created with the [wq start tool](https://wq.io/docs/setup).  The revision history for the initial version documents the full process:
 
1. [`ad70796`] Initialize with [wq start](https://wq.io/docs/setup) 1.0.0rc1
2. [`274dfc1`] Configure SSL with [LetsEncrypt](https://letsencrypt.org/)
3. [`8f89275`] Add [XLSForms](https://github.com/wq/xlsform-converter) for Category and Observation
4. [`cab2327`] Enable [wq/locate.js](https://wq.io/docs/locate-js)
5. Customize workflow:
   * [`3f244b4`] Use `<input type=tel>` rather than `<input type=number>` to get around precision issues with lat/long
   * [`25e263b`] Don't require authentication to submit a photo
   * [`ea70810`] Customize category screen (fix pluralization and ordering)
   * [`f3acccd`] Customize the links on the home screen
   * [`a0cd5d2`] Set defaults for date and location mode on observation screen
6. [`c7a6fac`] Integate the [cordova TensorFlow Plugin](https://github.com/heigeo/cordova-plugin-tensorflow)



[`ad70796`]: https://github.com/powered-by-wq/insideoutside.wq.io/commit/ad7079603d7e0328c3355bfddb22c73ada968d0f
[`274dfc1`]: https://github.com/powered-by-wq/insideoutside.wq.io/commit/274dfc182d9dddc0cf489b26f9926ecb695cae00
[`8f89275`]: https://github.com/powered-by-wq/insideoutside.wq.io/commit/8f8927545b0c9d75ec8efd17b96fce0a6420640b
[`cab2327`]: https://github.com/powered-by-wq/insideoutside.wq.io/commit/cab23278812415f598c7668d1a7089a630306eb2
[`3f244b4`]: https://github.com/powered-by-wq/insideoutside.wq.io/commit/3f244b47947b7d8d955863facfb4423cb8ba2f45
[`25e263b`]: https://github.com/powered-by-wq/insideoutside.wq.io/commit/25e263b32aa511fbdc77eefa18b83c7ad45a77cf
[`ea70810`]: https://github.com/powered-by-wq/insideoutside.wq.io/commit/ea70810a2f1e5e999f2907b69efbc41481344b7a
[`f3acccd`]: https://github.com/powered-by-wq/insideoutside.wq.io/commit/f3acccd58a5962de6138fc71f6d7ec8fc83484dc
[`a0cd5d2`]: https://github.com/powered-by-wq/insideoutside.wq.io/commit/a0cd5d26435c0afc695b100a3956fc256c32c601
[`c7a6fac`]: https://github.com/powered-by-wq/insideoutside.wq.io/commit/c7a6fac4e2f1f477cf7d701433bc90f42d4276bb
