"# django_mission_02-ttongs" 

- Inquiry 모델
```
    -카테고리 category
    -제목 title
    -이메일 email
    -이메일수신여부 email_rcv_yn
    -문자메세지(핸드폰번호) phone
    -문자수신여부 phone_rcv_yn
    -질문내용 question
    -이미지 image
    -생성자 writer
    -생성일시 created_at
```
- Answer 모델
```
    -답변내용 answer
    -참조문의글 ref_inquiry
    -생성자 writer
    -생성일시 created_at -> auto_now_add 사용
    -최종 수정자 final_writer
    -최종 수정일시 final_created_at -> auto_now 사용
```
