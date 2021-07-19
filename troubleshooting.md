# Troubleshooting

## Error 1
### TypeError: argument of type 'PosixPath' is not iterable
Ref: https://stackoverflow.com/questions/64634674/django-typeerror-argument-of-type-posixpath-is-not-iterable

## Error 2
### from Sentry.io/symbolicator
### Error parsing resolv.conf: ProtoError { kind: Msg(\"Malformed label:...
Check /etc/resolv.conf to remove lines that looks funny or has symbols like '@' (encoded) anywhere.

