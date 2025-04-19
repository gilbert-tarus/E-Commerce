from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect

from item.models import Item
from .forms import ConversationMessageForm
from .models import Conversation

@login_required
def new_conversation(request, pk): #item_p
    item = get_object_or_404(Item, pk = pk)

    if item.created_by == request.user:
        return redirect('dashboard:index')
    
    conversations = Conversation.objects.filter(item = item).filter(members__in=[request.user.id]) #To check if the id is of one of the members

    # Checking if there is already a conversation between the requesting user and the owner in oder to redirect that converstion.
    if conversations:
        # pass # Redirect to conversation
        return redirect('conversation:conversation_detail', pk = conversations.first().id )
    # Check if the form has been submitted
    if request.method == "POST":
        form = ConversationMessageForm(request.POST)

        if form.is_valid:
            conversation = Conversation.objects.create(item = item)

            #Adding you to the members list and the owner of the item to the members list.
            conversation.members.add(request.user)
            conversation.members.add(item.created_by)
            conversation.save()

            conversation_message = form.save(commit=False)
            conversation_message.conversation = conversation
            conversation_message.created_by = request.user
            conversation_message.save()

            return redirect('item:detail', pk = pk)
    
    else:
        form = ConversationMessageForm()

    return render(request, 'conversation/new.html',{
        'form': form
    })

@login_required
def inbox(request):
    # To view the conversations that has been sent to you / Custom to you
    conversations = Conversation.objects.filter(members__in=[request.user.id]) 

    return render(request, 'conversation/inbox.html',{
        'conversations': conversations
    })

# To be able to view the details of the conversions

@login_required
def conversation_detail(request, conversation_pk):#pk): #
    # Fetching the conversation
    conversation = Conversation.objects.filter(members__in=[request.user.id]).get(pk = conversation_pk)#pk) 

    if request.method == "POST":
        form = ConversationMessageForm(request.POST)

        if form.is_valid():
            conversation_message = form.save(commit=False)
            conversation_message.conversation = conversation
            conversation_message.created_by = request.user
            conversation_message.save()

            # To update the modified date
            conversation.save()

            return redirect('conversation:conversation_detail', conversation_pk = conversation.id )#pk = pk) #conversation_pk=pk(from db- conversation.id)
    else:
        form = ConversationMessageForm()

    return render(request, 'conversation/detail.html',{
        "conversation": conversation,
        "form" : form
    })


################### NEW ##########################

@login_required
def messages(request, pk = None): #message_pk=None
    # Fetch all the conversations for the logged-in user
    messages = Conversation.objects.filter(members__in=[request.user.id])


    conversation = None  # Set default as None
    if pk: #message_pk
        # Fetch the specific conversation if one is selected
        conversation = get_object_or_404(Conversation, pk = pk, members__in=[request.user.id]) #

    # Capturing new messages within the conversation

    if request.method == "POST":
        form = ConversationMessageForm(request.POST)

        if form.is_valid():
            conversation_message = form.save(commit=False)
            conversation_message.conversation = conversation
            conversation_message.created_by = request.user
            conversation_message.save()

            # To update the modified date
            conversation.save()

            return redirect('conversation:message_detail', pk = pk )#pk = pk) #conversation_pk=pk(from db- conversation.id)
    else:
        form = ConversationMessageForm()

    # Render both conversation list and conversation details (if any)
    return render(request, 'conversation/msgs_inbox.html', {
        'messages': messages,
        'conversation_i': conversation,  # Will be None if no conversation is selected
        'form': form
    })