from django.shortcuts import render,redirect

from django.contrib import messages
from django.contrib.auth import get_user_model


from .forms import Candidateform
from .models import Candidate 
from users.models import User
User = get_user_model()
# Create your views here.

def home(request):
    return render(request, "elections/homepage.html", {})


def addcandidate(request):
    
    if request.method=="POST":
        if request.user.is_authenticated:
            form=Candidateform(request.POST, request.FILES)
            if form.is_valid:
                form.save()
                candidate=Candidate.objects.get(name=request.POST["name"])
                if  candidate.email == request.user.email :
                    messages.success(request, "You are now a candidate")
                    return redirect('candidates')
                else :
                    candidate.delete()
                    messages.success(request , "This is not you!! , Please enter your login credentials")
                    return redirect('addcandidate')
            else:
                messages.success(request , "Please enter valid information.")
                return redirect('addcandidate')

        else:
            messages.success(request , "Please login first.")                        
            return redirect('login')
    else:
        form=Candidateform()
        return render(request, "elections/Newcandidate.html",{
                "form":form     
        })
                    


def vote1(request, candidate_id):
    candidate=Candidate.objects.get(pk=candidate_id)
    voter=request.user
    if not voter.vote_1_bool:
        candidate.votes+=5
        candidate.vote5+=1
        voter.vote1 = candidate
        voter.vote_1_bool=True
        candidate.save()
        voter.save()
        messages.success(request , "You have voted for First Preferance")
        return render(request, "elections/candidates.html",{
            "candidates":Candidate.objects.all()
        })
    else: 
        messages.success(request , "You have voted for this Preferance")
        return render(request, "elections/candidates.html",{
            "candidates":Candidate.objects.all()
        })

def vote2(request, candidate_id):
    
    candidate = Candidate.objects.get(pk=candidate_id)
    voter = request.user
    if not voter.vote_2_bool:
        candidate.votes+=3
        candidate.vote3+=1
        voter.vote2 = candidate
        voter.vote_2_bool=True
        candidate.save()
        voter.save()
        messages.success(request , "You have voted for Second Preferance")
        return render(request, "elections/candidates.html",{
            "candidates":Candidate.objects.all()
        })
                
    else:
        messages.success(request , "You have voted for this Preferance")
        return render(request, "elections/candidates.html",{
            "candidates":Candidate.objects.all()
        })

def vote3(request, candidate_id):
    candidate=Candidate.objects.get(pk=candidate_id)
    voter=request.user
    if not voter.vote_3_bool:
        candidate.votes += 1
        candidate.vote1+=1
        voter.vote3 = candidate
        voter.vote_3_bool=True
        candidate.save()
        voter.save()
        messages.success(request , "You have voted for Third Preferance")
        return render(request, "elections/candidates.html",{
            "candidates":Candidate.objects.all()
        })
    else:
        messages.success(request , "You have voted for this Preferance")
        return render(request, "elections/candidates.html",{
            "candidates":Candidate.objects.all()
        })



def all_candidates(request):
    candidates=Candidate.objects.all()
    return render(request, "elections/candidates.html",{
        "candidates":candidates
    })





def result(request):
    branch = request.user.branch
    all_candidates= Candidate.objects.filter(branch = branch)
    votes=[]
    for cand in all_candidates:
        v=cand.votes
        votes.append(v)

    winner_votes=max(votes)
    winner_candidates=Candidate.objects.filter(votes=winner_votes)
    vote_5=[]
    vote_3=[]
    vote_1=[]
    for can in winner_candidates:
        vote_5.append(can.vote5)
        vote_3.append(can.vote3)
        vote_1.append(can.vote1)
    maxvote5=max(vote_5)
    maxvote3=max(vote_3)
    maxvote1=max(vote_1)
    win_can5=Candidate.objects.filter(vote5=maxvote5)
    if win_can5.count()>1:
        for can in win_can5:
            vote3.add(can.vote3)
        maxvote3=max(vote_3)
        win_can3=Candidate.objects.filter(vote3=maxvote3)
        if win_can3.count()>1:
            for can in win_can3:
                vote1.add(can.vote1)
            maxvote1=max(vote_1)
            win_can1=Candidate.objects.get(vote1=maxvote1)
            return render(request, "elections/result.html",{
        "winner":win_can1,
    }) 
        else:
            win_can3=Candidate.objects.get(vote3=maxvote3)
            return render(request, "elections/result.html",{
        "winner":win_can3,
        
    })    

    else:
        win_can = Candidate.objects.get(votes=winner_votes)
        return render(request, "elections/result.html",{    
        "winner":win_can,
        
    })    



def update(request, candidate_id):
    candidate=Candidate.objects.get(pk=candidate_id)
    if request.method == "POST": 
        form = Candidateform(request.POST or None ,  instance=candidate)
        if form.is_valid():
            form.save()

            return render(request, "elections/candidates.html",{
                "candidates" : Candidate.objects.all
            })
    else:
        form = Candidateform(instance=candidate)
        return render(request , "elections/Newcandidate.html", {
            "form" : form
        } )



            