webpackJsonp([1],[
/* 0 */
/***/ (function(module, exports, __webpack_require__) {

	eval("/* REACT HOT LOADER */ if (false) { (function () { var ReactHotAPI = require(\"E:\\\\login\\\\node_modules\\\\react-hot-api\\\\modules\\\\index.js\"), RootInstanceProvider = require(\"E:\\\\login\\\\node_modules\\\\react-hot-loader\\\\RootInstanceProvider.js\"), ReactMount = require(\"react/lib/ReactMount\"), React = require(\"react\"); module.makeHot = module.hot.data ? module.hot.data.makeHot : ReactHotAPI(function () { return RootInstanceProvider.getRootInstances(ReactMount); }, React); })(); } try { (function () {\n\n'use strict';\n\nvar _createClass = function () { function defineProperties(target, props) { for (var i = 0; i < props.length; i++) { var descriptor = props[i]; descriptor.enumerable = descriptor.enumerable || false; descriptor.configurable = true; if (\"value\" in descriptor) descriptor.writable = true; Object.defineProperty(target, descriptor.key, descriptor); } } return function (Constructor, protoProps, staticProps) { if (protoProps) defineProperties(Constructor.prototype, protoProps); if (staticProps) defineProperties(Constructor, staticProps); return Constructor; }; }();\n\nvar _react = __webpack_require__(1);\n\nvar _react2 = _interopRequireDefault(_react);\n\nvar _reactDom = __webpack_require__(8);\n\nfunction _interopRequireDefault(obj) { return obj && obj.__esModule ? obj : { default: obj }; }\n\nfunction _asyncToGenerator(fn) { return function () { var gen = fn.apply(this, arguments); return new Promise(function (resolve, reject) { function step(key, arg) { try { var info = gen[key](arg); var value = info.value; } catch (error) { reject(error); return; } if (info.done) { resolve(value); } else { return Promise.resolve(value).then(function (value) { step(\"next\", value); }, function (err) { step(\"throw\", err); }); } } return step(\"next\"); }); }; }\n\nfunction _classCallCheck(instance, Constructor) { if (!(instance instanceof Constructor)) { throw new TypeError(\"Cannot call a class as a function\"); } }\n\nfunction _possibleConstructorReturn(self, call) { if (!self) { throw new ReferenceError(\"this hasn't been initialised - super() hasn't been called\"); } return call && (typeof call === \"object\" || typeof call === \"function\") ? call : self; }\n\nfunction _inherits(subClass, superClass) { if (typeof superClass !== \"function\" && superClass !== null) { throw new TypeError(\"Super expression must either be null or a function, not \" + typeof superClass); } subClass.prototype = Object.create(superClass && superClass.prototype, { constructor: { value: subClass, enumerable: false, writable: true, configurable: true } }); if (superClass) Object.setPrototypeOf ? Object.setPrototypeOf(subClass, superClass) : subClass.__proto__ = superClass; }\n\nvar videoType = 'video/webm';\n\nvar HomePage = function (_React$Component) {\n  _inherits(HomePage, _React$Component);\n\n  function HomePage(props) {\n    _classCallCheck(this, HomePage);\n\n    var _this = _possibleConstructorReturn(this, (HomePage.__proto__ || Object.getPrototypeOf(HomePage)).call(this, props));\n\n    _this.state = {\n      recording: false,\n      videos: []\n    };\n    return _this;\n  }\n\n  _createClass(HomePage, [{\n    key: 'componentDidMount',\n    value: function () {\n      var _ref = _asyncToGenerator( /*#__PURE__*/regeneratorRuntime.mark(function _callee() {\n        var _this2 = this;\n\n        var stream;\n        return regeneratorRuntime.wrap(function _callee$(_context) {\n          while (1) {\n            switch (_context.prev = _context.next) {\n              case 0:\n                _context.next = 2;\n                return navigator.mediaDevices.getUserMedia({ video: true, audio: true });\n\n              case 2:\n                stream = _context.sent;\n\n                // show it to user\n                this.video.src = window.URL.createObjectURL(stream);\n                this.video.play();\n                // init recording\n                this.mediaRecorder = new MediaRecorder(stream, {\n                  mimeType: videoType\n                });\n                // init data storage for video chunks\n                this.chunks = [];\n                // listen for data from media recorder\n                this.mediaRecorder.ondataavailable = function (e) {\n                  if (e.data && e.data.size > 0) {\n                    _this2.chunks.push(e.data);\n                  }\n                };\n\n              case 8:\n              case 'end':\n                return _context.stop();\n            }\n          }\n        }, _callee, this);\n      }));\n\n      function componentDidMount() {\n        return _ref.apply(this, arguments);\n      }\n\n      return componentDidMount;\n    }()\n  }, {\n    key: 'startRecording',\n    value: function startRecording(e) {\n      e.preventDefault();\n      // wipe old data chunks\n      this.chunks = [];\n      // start recorder with 10ms buffer\n      this.mediaRecorder.start(10);\n      // say that we're recording\n      this.setState({ recording: true });\n    }\n  }, {\n    key: 'stopRecording',\n    value: function stopRecording(e) {\n      e.preventDefault();\n      // stop the recorder\n      this.mediaRecorder.stop();\n      // say that we're not recording\n      this.setState({ recording: false });\n      // save the video to memory\n      this.saveVideo();\n    }\n  }, {\n    key: 'saveVideo',\n    value: function saveVideo() {\n      // convert saved chunks to blob\n      var blob = new Blob(this.chunks, { type: videoType });\n      // generate video url from blob\n      var videoURL = window.URL.createObjectURL(blob);\n      // append videoURL to list of saved videos for rendering\n      var videos = this.state.videos.concat([videoURL]);\n      this.setState({ videos: videos });\n    }\n  }, {\n    key: 'deleteVideo',\n    value: function deleteVideo(videoURL) {\n      // filter out current videoURL from the list of saved videos\n      var videos = this.state.videos.filter(function (v) {\n        return v !== videoURL;\n      });\n      this.setState({ videos: videos });\n    }\n  }, {\n    key: 'render',\n    value: function render() {\n      var _this3 = this;\n\n      var _state = this.state,\n          recording = _state.recording,\n          videos = _state.videos;\n\n      return _react2.default.createElement(\n        'div',\n        { className: 'camera' },\n        _react2.default.createElement(\n          'video',\n          {\n            style: { width: 400 },\n            ref: function ref(v) {\n              _this3.video = v;\n            } },\n          'Video stream not available.'\n        ),\n        _react2.default.createElement(\n          'div',\n          null,\n          !recording && _react2.default.createElement(\n            'button',\n            { onClick: function onClick(e) {\n                return _this3.startRecording(e);\n              } },\n            'Record'\n          ),\n          recording && _react2.default.createElement(\n            'button',\n            { onClick: function onClick(e) {\n                return _this3.stopRecording(e);\n              } },\n            'Stop'\n          )\n        ),\n        _react2.default.createElement(\n          'div',\n          null,\n          _react2.default.createElement(\n            'h3',\n            null,\n            'Recorded videos:'\n          ),\n          videos.map(function (videoURL, i) {\n            return _react2.default.createElement(\n              'div',\n              { key: 'video_' + i },\n              _react2.default.createElement('video', { style: { width: 200 }, src: videoURL, autoPlay: true, loop: true }),\n              _react2.default.createElement(\n                'div',\n                null,\n                _react2.default.createElement(\n                  'button',\n                  { onClick: function onClick() {\n                      return _this3.deleteVideo(videoURL);\n                    } },\n                  'Delete'\n                ),\n                _react2.default.createElement(\n                  'a',\n                  { href: videoURL },\n                  'Download'\n                )\n              )\n            );\n          })\n        )\n      );\n    }\n  }]);\n\n  return HomePage;\n}(_react2.default.Component);\n\n(0, _reactDom.render)(_react2.default.createElement(App2, null), document.getElementById('App2'));\n\n/* REACT HOT LOADER */ }).call(this); } finally { if (false) { (function () { var foundReactClasses = module.hot.data && module.hot.data.foundReactClasses || false; if (module.exports && module.makeHot) { var makeExportsHot = require(\"E:\\\\login\\\\node_modules\\\\react-hot-loader\\\\makeExportsHot.js\"); if (makeExportsHot(module, require(\"react\"))) { foundReactClasses = true; } var shouldAcceptModule = true && foundReactClasses; if (shouldAcceptModule) { module.hot.accept(function (err) { if (err) { console.error(\"Cannot apply hot update to \" + \"vedio.js\" + \": \" + err.message); } }); } } module.hot.dispose(function (data) { data.makeHot = module.makeHot; data.foundReactClasses = foundReactClasses; }); })(); } }\n//# sourceMappingURL=data:application/json;charset=utf-8;base64,eyJ2ZXJzaW9uIjozLCJzb3VyY2VzIjpbIndlYnBhY2s6Ly8vLi9zdGF0aWMvanMvdmVkaW8uanM/OWFiOSJdLCJuYW1lcyI6WyJ2aWRlb1R5cGUiLCJIb21lUGFnZSIsInByb3BzIiwic3RhdGUiLCJyZWNvcmRpbmciLCJ2aWRlb3MiLCJuYXZpZ2F0b3IiLCJtZWRpYURldmljZXMiLCJnZXRVc2VyTWVkaWEiLCJ2aWRlbyIsImF1ZGlvIiwic3RyZWFtIiwic3JjIiwid2luZG93IiwiVVJMIiwiY3JlYXRlT2JqZWN0VVJMIiwicGxheSIsIm1lZGlhUmVjb3JkZXIiLCJNZWRpYVJlY29yZGVyIiwibWltZVR5cGUiLCJjaHVua3MiLCJvbmRhdGFhdmFpbGFibGUiLCJlIiwiZGF0YSIsInNpemUiLCJwdXNoIiwicHJldmVudERlZmF1bHQiLCJzdGFydCIsInNldFN0YXRlIiwic3RvcCIsInNhdmVWaWRlbyIsImJsb2IiLCJCbG9iIiwidHlwZSIsInZpZGVvVVJMIiwiY29uY2F0IiwiZmlsdGVyIiwidiIsIndpZHRoIiwic3RhcnRSZWNvcmRpbmciLCJzdG9wUmVjb3JkaW5nIiwibWFwIiwiaSIsImRlbGV0ZVZpZGVvIiwiUmVhY3QiLCJDb21wb25lbnQiLCJkb2N1bWVudCIsImdldEVsZW1lbnRCeUlkIl0sIm1hcHBpbmdzIjoiOzs7Ozs7QUFBQTs7OztBQUNBOzs7Ozs7Ozs7Ozs7QUFDQSxJQUFNQSxZQUFZLFlBQWxCOztJQUVNQyxROzs7QUFDSixvQkFBWUMsS0FBWixFQUFtQjtBQUFBOztBQUFBLG9IQUNYQSxLQURXOztBQUVqQixVQUFLQyxLQUFMLEdBQWE7QUFDWEMsaUJBQVcsS0FEQTtBQUVYQyxjQUFRO0FBRkcsS0FBYjtBQUZpQjtBQU1sQjs7Ozs7Ozs7Ozs7Ozs7dUJBRXNCQyxVQUFVQyxZQUFWLENBQXVCQyxZQUF2QixDQUFvQyxFQUFDQyxPQUFPLElBQVIsRUFBY0MsT0FBTyxJQUFyQixFQUFwQyxDOzs7QUFBZkMsc0I7O0FBQ047QUFDQSxxQkFBS0YsS0FBTCxDQUFXRyxHQUFYLEdBQWlC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QixLQUFLSixRQUFqQyxFQUEyQyxjQUEzQyxFQUFvRCxVQUFwRCxHQURGO0FBRUU7QUFBQTtBQUFBO0FBQ0U7QUFBQTtBQUFBLG9CQUFRLFNBQVM7QUFBQSw2QkFBTSxPQUFLUyxXQUFMLENBQWlCVCxRQUFqQixDQUFOO0FBQUEscUJBQWpCO0FBQUE7QUFBQSxpQkFERjtBQUVFO0FBQUE7QUFBQSxvQkFBRyxNQUFNQSxRQUFUO0FBQUE7QUFBQTtBQUZGO0FBRkYsYUFEVTtBQUFBLFdBQVg7QUFGSDtBQVpGLE9BREY7QUEyQkQ7Ozs7RUF2Rm9CVSxnQkFBTUMsUzs7QUEyRjVCLHNCQUFPLDhCQUFDLElBQUQsT0FBUCxFQUFnQkMsU0FBU0MsY0FBVCxDQUF3QixNQUF4QixDQUFoQixFIiwiZmlsZSI6IjAuanMiLCJzb3VyY2VzQ29udGVudCI6WyJpbXBvcnQgUmVhY3QgZnJvbSAncmVhY3QnO1xyXG5pbXBvcnQgeyByZW5kZXIgfSBmcm9tIFwicmVhY3QtZG9tXCJcclxuY29uc3QgdmlkZW9UeXBlID0gJ3ZpZGVvL3dlYm0nO1xyXG5cclxuY2xhc3MgSG9tZVBhZ2UgZXh0ZW5kcyBSZWFjdC5Db21wb25lbnQge1xyXG4gIGNvbnN0cnVjdG9yKHByb3BzKSB7XHJcbiAgICBzdXBlcihwcm9wcyk7XHJcbiAgICB0aGlzLnN0YXRlID0ge1xyXG4gICAgICByZWNvcmRpbmc6IGZhbHNlLFxyXG4gICAgICB2aWRlb3M6IFtdLFxyXG4gICAgfTtcclxuICB9XHJcbiAgYXN5bmMgY29tcG9uZW50RGlkTW91bnQoKSB7XHJcbiAgICBjb25zdCBzdHJlYW0gPSBhd2FpdCBuYXZpZ2F0b3IubWVkaWFEZXZpY2VzLmdldFVzZXJNZWRpYSh7dmlkZW86IHRydWUsIGF1ZGlvOiB0cnVlfSk7XHJcbiAgICAvLyBzaG93IGl0IHRvIHVzZXJcclxuICAgIHRoaXMudmlkZW8uc3JjID0gd2luZG93LlVSTC5jcmVhdGVPYmplY3RVUkwoc3RyZWFtKTtcclxuICAgIHRoaXMudmlkZW8ucGxheSgpO1xyXG4gICAgLy8gaW5pdCByZWNvcmRpbmdcclxuICAgIHRoaXMubWVkaWFSZWNvcmRlciA9IG5ldyBNZWRpYVJlY29yZGVyKHN0cmVhbSwge1xyXG4gICAgICBtaW1lVHlwZTogdmlkZW9UeXBlLFxyXG4gICAgfSk7XHJcbiAgICAvLyBpbml0IGRhdGEgc3RvcmFnZSBmb3IgdmlkZW8gY2h1bmtzXHJcbiAgICB0aGlzLmNodW5rcyA9IFtdO1xyXG4gICAgLy8gbGlzdGVuIGZvciBkYXRhIGZyb20gbWVkaWEgcmVjb3JkZXJcclxuICAgIHRoaXMubWVkaWFSZWNvcmRlci5vbmRhdGFhdmFpbGFibGUgPSBlID0+IHtcclxuICAgICAgaWYgKGUuZGF0YSAmJiBlLmRhdGEuc2l6ZSA+IDApIHtcclxuICAgICAgICB0aGlzLmNodW5rcy5wdXNoKGUuZGF0YSk7XHJcbiAgICAgIH1cclxuICAgIH07XHJcbiAgfVxyXG4gIHN0YXJ0UmVjb3JkaW5nKGUpIHtcclxuICAgIGUucHJldmVudERlZmF1bHQoKTtcclxuICAgIC8vIHdpcGUgb2xkIGRhdGEgY2h1bmtzXHJcbiAgICB0aGlzLmNodW5rcyA9IFtdO1xyXG4gICAgLy8gc3RhcnQgcmVjb3JkZXIgd2l0aCAxMG1zIGJ1ZmZlclxyXG4gICAgdGhpcy5tZWRpYVJlY29yZGVyLnN0YXJ0KDEwKTtcclxuICAgIC8vIHNheSB0aGF0IHdlJ3JlIHJlY29yZGluZ1xyXG4gICAgdGhpcy5zZXRTdGF0ZSh7cmVjb3JkaW5nOiB0cnVlfSk7XHJcbiAgfVxyXG4gIHN0b3BSZWNvcmRpbmcoZSkge1xyXG4gICAgZS5wcmV2ZW50RGVmYXVsdCgpO1xyXG4gICAgLy8gc3RvcCB0aGUgcmVjb3JkZXJcclxuICAgIHRoaXMubWVkaWFSZWNvcmRlci5zdG9wKCk7XHJcbiAgICAvLyBzYXkgdGhhdCB3ZSdyZSBub3QgcmVjb3JkaW5nXHJcbiAgICB0aGlzLnNldFN0YXRlKHtyZWNvcmRpbmc6IGZhbHNlfSk7XHJcbiAgICAvLyBzYXZlIHRoZSB2aWRlbyB0byBtZW1vcnlcclxuICAgIHRoaXMuc2F2ZVZpZGVvKCk7XHJcbiAgfVxyXG4gIHNhdmVWaWRlbygpIHtcclxuICAgIC8vIGNvbnZlcnQgc2F2ZWQgY2h1bmtzIHRvIGJsb2JcclxuICAgIGNvbnN0IGJsb2IgPSBuZXcgQmxvYih0aGlzLmNodW5rcywge3R5cGU6IHZpZGVvVHlwZX0pO1xyXG4gICAgLy8gZ2VuZXJhdGUgdmlkZW8gdXJsIGZyb20gYmxvYlxyXG4gICAgY29uc3QgdmlkZW9VUkwgPSB3aW5kb3cuVVJMLmNyZWF0ZU9iamVjdFVSTChibG9iKTtcclxuICAgIC8vIGFwcGVuZCB2aWRlb1VSTCB0byBsaXN0IG9mIHNhdmVkIHZpZGVvcyBmb3IgcmVuZGVyaW5nXHJcbiAgICBjb25zdCB2aWRlb3MgPSB0aGlzLnN0YXRlLnZpZGVvcy5jb25jYXQoW3ZpZGVvVVJMXSk7XHJcbiAgICB0aGlzLnNldFN0YXRlKHt2aWRlb3N9KTtcclxuICB9XHJcbiAgZGVsZXRlVmlkZW8odmlkZW9VUkwpIHtcclxuICAgIC8vIGZpbHRlciBvdXQgY3VycmVudCB2aWRlb1VSTCBmcm9tIHRoZSBsaXN0IG9mIHNhdmVkIHZpZGVvc1xyXG4gICAgY29uc3QgdmlkZW9zID0gdGhpcy5zdGF0ZS52aWRlb3MuZmlsdGVyKHYgPT4gdiAhPT0gdmlkZW9VUkwpO1xyXG4gICAgdGhpcy5zZXRTdGF0ZSh7dmlkZW9zfSk7XHJcbiAgfVxyXG4gIHJlbmRlcigpIHtcclxuICAgIGNvbnN0IHtyZWNvcmRpbmcsIHZpZGVvc30gPSB0aGlzLnN0YXRlO1xyXG4gICAgcmV0dXJuIChcclxuICAgICAgPGRpdiBjbGFzc05hbWU9XCJjYW1lcmFcIj5cclxuICAgICAgICA8dmlkZW9cclxuICAgICAgICAgIHN0eWxlPXt7d2lkdGg6IDQwMH19XHJcbiAgICAgICAgICByZWY9e3YgPT4ge1xyXG4gICAgICAgICAgICB0aGlzLnZpZGVvID0gdjtcclxuICAgICAgICAgIH19PlxyXG4gICAgICAgICAgVmlkZW8gc3RyZWFtIG5vdCBhdmFpbGFibGUuXHJcbiAgICAgICAgPC92aWRlbz5cclxuICAgICAgICA8ZGl2PlxyXG4gICAgICAgICAgeyFyZWNvcmRpbmcgJiYgPGJ1dHRvbiBvbkNsaWNrPXtlID0+IHRoaXMuc3RhcnRSZWNvcmRpbmcoZSl9PlJlY29yZDwvYnV0dG9uPn1cclxuICAgICAgICAgIHtyZWNvcmRpbmcgJiYgPGJ1dHRvbiBvbkNsaWNrPXtlID0+IHRoaXMuc3RvcFJlY29yZGluZyhlKX0+U3RvcDwvYnV0dG9uPn1cclxuICAgICAgICA8L2Rpdj5cclxuICAgICAgICA8ZGl2PlxyXG4gICAgICAgICAgPGgzPlJlY29yZGVkIHZpZGVvczo8L2gzPlxyXG4gICAgICAgICAge3ZpZGVvcy5tYXAoKHZpZGVvVVJMLCBpKSA9PiAoXHJcbiAgICAgICAgICAgIDxkaXYga2V5PXtgdmlkZW9fJHtpfWB9PlxyXG4gICAgICAgICAgICAgIDx2aWRlbyBzdHlsZT17e3dpZHRoOiAyMDB9fSBzcmM9e3ZpZGVvVVJMfSBhdXRvUGxheSBsb29wIC8+XHJcbiAgICAgICAgICAgICAgPGRpdj5cclxuICAgICAgICAgICAgICAgIDxidXR0b24gb25DbGljaz17KCkgPT4gdGhpcy5kZWxldGVWaWRlbyh2aWRlb1VSTCl9PkRlbGV0ZTwvYnV0dG9uPlxyXG4gICAgICAgICAgICAgICAgPGEgaHJlZj17dmlkZW9VUkx9PkRvd25sb2FkPC9hPlxyXG4gICAgICAgICAgICAgIDwvZGl2PlxyXG4gICAgICAgICAgICA8L2Rpdj5cclxuICAgICAgICAgICkpfVxyXG4gICAgICAgIDwvZGl2PlxyXG4gICAgICA8L2Rpdj5cclxuICAgIClcclxuICB9XHJcbn1cclxuXHJcblxyXG4gcmVuZGVyKDxBcHAyLz4sIGRvY3VtZW50LmdldEVsZW1lbnRCeUlkKCdBcHAyJykpXHJcblxuXG5cbi8vIFdFQlBBQ0sgRk9PVEVSIC8vXG4vLyAuL3N0YXRpYy9qcy92ZWRpby5qcyJdLCJzb3VyY2VSb290IjoiIn0=");

/***/ })
]);