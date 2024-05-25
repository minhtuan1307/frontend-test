import { Component, OnInit } from '@angular/core';
import { ChatService } from '../../services/chat.service';

@Component({
  selector: 'app-chat',
  templateUrl: './chat.component.html',
  styleUrl: './chat.component.css'
})
export class ChatComponent implements OnInit {
  ngOnInit(): void {
    this.listMessages();
  }
  public message: string = "";
  public messages: any = [];

  constructor(private chatService: ChatService){

  }

  public sendMessage(){
    this.chatService.sendMessage(this.message);
    this.messages.push(this.message);
    this.message = '';
  }
  public listMessages(){
    
    this.chatService.listMessages().subscribe((data: any) => {
      console.log('#Debug 1');
      console.log(data);
      this.messages.push(data.data)
    });
  }
}
