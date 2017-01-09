/* ==========================================================================
   Scripts for Email Signup organism.
   ========================================================================== */

'use strict';

var FormSubmit = require( '../../organisms/FormSubmit.js' );
var validators = require( '../../modules/util/validators' );
var webStorageProxy = require( '../../modules/util/web-storage-proxy' );
var isArray = require( '../../modules/util/type-checkers' ).isArray;

var BASE_CLASS = 'o-email-signup';
var EMAIL_LIST_KEY = 'emailSignups';

function emailValidation( fields ) {
  if ( fields.email && !fields.email.value ) {
  	return 'Please enter an email address.';
  } 
  return validators.email( fields.email ).msg;
}

function storeEmailListCode( code ) {
  var emailSignups = webStorageProxy.getItem( EMAIL_LIST_KEY, localStorage );
  try {
    emailSignups = JSON.parse( emailSignups );
  } catch (e) {}
  if ( !isArray( emailSignups ) ) {
    emailSignups = [ code ];
  } else if ( emailSignups.indexOf( code ) === -1 ) {
    emailSignups.push( code );
  }
  webStorageProxy.setItem( EMAIL_LIST_KEY, JSON.stringify( emailSignups ), localStorage );
}

var formSubmit = new FormSubmit(
  document.body.querySelector( '.' + BASE_CLASS ),
  BASE_CLASS,
  { validator: emailValidation }
);

formSubmit.addEventListener( 'success', function onEmailSignupSuccess( event ) {
  var form = event.target;
  var input = form.querySelector( 'input[name="code"]' );
  storeEmailListCode( input.value );
} );

formSubmit.init();
