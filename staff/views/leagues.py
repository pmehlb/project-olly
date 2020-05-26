from django.contrib import messages
from django.shortcuts import render, redirect
#from django.views.generic import View

#from matches.models import MatchReport, MatchDispute, Match, MapChoice, MapPoolChoice
from staff.forms import *


def create_league(request):
    user = UserProfile.objects.get(user__username=request.user.username)
    allowed = ['superadmin', 'admin']
    if user.user_type not in allowed:
        return render(request, 'staff/permissiondenied.html')
    else:
        if request.method == 'GET':
            form = CreateLeagueForm
            return render(request, 'staff/leagues/league_create.html', {'form': form})
        else:
            # the form is posting, lets start validating
            form = CreateLeagueForm(request.POST, request.FILES)
            if form.is_valid():
                league = form.instance
                league.save()
                messages.success(request, 'Created League')
                return redirect('staff:list_league')
            else:
                form = CreateLeagueForm(request.POST)
                return render(request, 'staff/leagues/league_create.html', {'form': form})


def list_league(request):
    user = UserProfile.objects.get(user__username=request.user.username)
    allowed = ['superadmin', 'admin']
    if user.user_type not in allowed:
        return render(request, 'staff/permissiondenied.html')
    else:
        leagues = League.objects.all()
        return render(request, 'staff/leagues/league_list.html', {'leagues': leagues})


def detail_league(request, pk):
    user = UserProfile.objects.get(user__username=request.user.username)
    allowed = ['superadmin', 'admin']
    if user.user_type not in allowed:
        return render(request, 'staff/permissiondenied.html')
    else:
        league = League.objects.get(pk=pk)
        divisions = league.divisions
        return render(request, 'staff/leagues/league_detail.html', {'league': league})


# list all the teams in the league and the divisions
def league_teams(request, pk):
    user = UserProfile.objects.get(user__username=request.user.username)
    allowed = ['superadmin', 'admin']
    if user.user_type not in allowed:
        return render(request, 'staff/permissiondenied.html')
    else:
        league = League.objects.get(pk=pk)
        divisions = league.divisions
        return render(request, 'staff/leagues/league_teams.html', {'league': league, 'divisions': divisions})


# used for adding teams to a league before the league is launched
def league_teams_add(request, pk):
    user = UserProfile.objects.get(user__username=request.user.username)
    allowed = ['superadmin', 'admin']
    if user.user_type not in allowed:
        return render(request, 'staff/permissiondenied.hmtl')
    else:
        league = League.objects.get(pk=pk)
        return render(request, 'staff/leagues/league_teams_add.html', {'league': league})


def edit_league(request, pk):
    user = UserProfile.objects.get(user__username=request.user.username)
    allowed = ['superadmin', 'admin']
    if user.user_type not in allowed:
        return render(request, 'staff/permissiondenied.html')
    else:
        if request.method == 'POST':
            league = League.objects.get(pk=pk)
            form = CreateLeagueForm(request.POST, request.FILES, instance=league)
            if form.is_valid():
                form.save()
                messages.success(request, 'League has been updated')
                return redirect('staff:list_league')
            else:
                messages.error(request, 'Form validation error')
                return redirect('staff:list_league')
        else:
            league = League.objects.get(pk=pk)
            form = CreateLeagueForm(instance=league)
            return render(request, 'staff/leagues/league_edit.html', {'form': form, 'pk':pk, 'league':league})


def list_league_settings(request):
    user = UserProfile.objects.get(user__username=request.user.username)
    allowed = ['superadmin', 'admin']
    if user.user_type not in allowed:
        return render(request, 'staff/permissiondenied.html')
    else:
        settings = LeagueSettings.objects.all()
        return render(request, 'staff/leagues/league_settings_list.html', {'settings': settings})


def create_league_settings(request):
    user = UserProfile.objects.get(user__username=request.user.username)
    allowed = ['superadmin', 'admin']
    if user.user_type not in allowed:
        return render(request, 'staff/permissiondenied.html')
    else:
        if request.method == 'GET':
            form = CreateLeagueSettingsForm
            return render(request, 'staff/leagues/league_settings_create.html', {'form': form})
        else:
            form = CreateLeagueSettingsForm(request.POST)
            if form.is_valid():
                settings = form.instance
                settings.save()
                messages.success(request, 'Created League Settings')
                return redirect('staff:list_league_settings')
            else:
                messages.error(request, 'A form validation error has occured')
                form = CreateLeagueSettingsForm(request.POST)
                return render(request, 'staff/leagues/league_settings_create.html', {'form': form})


def edit_league_settings(request, pk):
    user = UserProfile.objects.get(user__username=request.user.username)
    allowed = ['superadmin', 'admin']
    if user.user_type not in allowed:
        return render(request, 'staff/permissiondenied.html')
    else:
        if request.method == 'POST':
            league = LeagueSettings.objects.get(pk=pk)
            form = EditLeagueSettingsForm(request.POST, request.FILES, instance=league)
            if form.is_valid():
                form.save()
                messages.success(request, 'League Settings has been updated')
                return redirect('staff:list_league_settings')
            else:
                return render(request, 'staff/leagues/league_settings_edit.html', {'form': form})
        else:
            league = LeagueSettings.objects.get(pk=pk)
            form = EditLeagueSettingsForm(instance=league)
            return render(request, 'staff/leagues/league_settings_edit.html', {'form': form, 'pk': pk})


def detail_league_settings(request, pk):
    user = UserProfile.objects.get(user__username=request.user.username)
    allowed = ['superadmin', 'admin']
    if user.user_type not in allowed:
        return render(request, 'staff/permissiondenied.html')
    else:
        settings = LeagueSettings.objects.get(pk=pk)
        return render(request, 'staff/leagues/league_settings_detail.html', {'settings': settings})


def launch_league(request, pk):
    user = UserProfile.objects.get(user__username=request.user.username)
    allowed = ['superadmin', 'admin']
    if user.user_type not in allowed:
        return render(request, 'staff/permissiondenied.html')
    else:
        league = League.objects.get(pk=pk)
        settings = league.settings
