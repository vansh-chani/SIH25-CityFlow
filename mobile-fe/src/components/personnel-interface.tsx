"use client"

import { useState } from "react"
import { Card, CardContent, CardHeader, CardTitle } from "@/components/ui/card"
import { Button } from "@/components/ui/button"
import { Badge } from "@/components/ui/badge"
import { Avatar, AvatarFallback } from "@/components/ui/avatar"
import {
  MapPin,
  Navigation,
  AlertTriangle,
  CheckCircle,
  Clock,
  Radio,
  Shield,
  Bell,
  MessageSquare,
  Phone,
} from "lucide-react"

export function PersonnelInterface() {
  const [currentAssignment, setCurrentAssignment] = useState({
    id: "A001",
    type: "Traffic Control",
    location: "Main St & 5th Avenue",
    priority: "High",
    description: "Manage traffic flow during rush hour. Monitor intersection for congestion.",
    estimatedDuration: "2 hours",
    status: "Active",
  })

  const notifications = [
    { id: 1, type: "New Assignment", message: "Traffic control needed at Oak Street", time: "2 min ago", urgent: true },
    { id: 2, type: "Update", message: "Road closure on Highway 101 extended", time: "15 min ago", urgent: false },
    { id: 3, type: "Weather Alert", message: "Heavy rain expected in 30 minutes", time: "25 min ago", urgent: true },
  ]

  const nearbyIncidents = [
    { id: 1, type: "Accident", location: "2nd St & Broadway", distance: "0.3 miles", severity: "Minor" },
    { id: 2, type: "Road Work", location: "Industrial Ave", distance: "0.8 miles", severity: "Low" },
  ]

  return (
    <div className="min-h-screen bg-background">
      {/* Header */}
      <div className="bg-card border-b border-border p-4">
        <div className="flex items-center justify-between">
          <div className="flex items-center gap-3">
            <Avatar className="bg-orange-100">
              <AvatarFallback className="bg-orange-500 text-white font-semibold">OJ</AvatarFallback>
            </Avatar>
            <div>
              <h1 className="font-semibold text-foreground">Officer Johnson</h1>
              <p className="text-sm text-muted-foreground">Traffic Personnel • ID: TP001</p>
            </div>
          </div>
          <div className="flex items-center gap-2">
            <Button variant="outline" size="sm">
              <Bell className="w-4 h-4" />
            </Button>
            <Badge variant="default" className="bg-orange-500 hover:bg-orange-600">
              <Shield className="w-3 h-3 mr-1" />
              On Duty
            </Badge>
          </div>
        </div>
      </div>

      <div className="p-4 space-y-4">
        {/* Current Location */}
        <Card className="bg-orange-50 border-orange-200">
          <CardContent className="p-4">
            <div className="flex items-center gap-3">
              <div className="bg-orange-500 p-2 rounded-full">
                <MapPin className="w-4 h-4 text-white" />
              </div>
              <div className="flex-1">
                <p className="font-medium text-foreground">Current Location</p>
                <p className="text-sm text-muted-foreground">Main St & 5th Avenue</p>
              </div>
              <Button variant="outline" size="sm">
                <Navigation className="w-4 h-4" />
              </Button>
            </div>
          </CardContent>
        </Card>

        {/* Active Assignment */}
        <Card>
          <CardHeader className="pb-3">
            <CardTitle className="flex items-center justify-between">
              <span className="flex items-center gap-2">
                <AlertTriangle className="w-5 h-5 text-orange-500" />
                Active Assignment
              </span>
              <Badge variant="destructive" className="bg-orange-500 hover:bg-orange-600">
                {currentAssignment.priority}
              </Badge>
            </CardTitle>
          </CardHeader>
          <CardContent className="space-y-4">
            <div>
              <h3 className="font-semibold text-foreground">{currentAssignment.type}</h3>
              <p className="text-sm text-muted-foreground flex items-center gap-1 mt-1">
                <MapPin className="w-3 h-3" />
                {currentAssignment.location}
              </p>
            </div>

            <p className="text-sm text-foreground">{currentAssignment.description}</p>

            <div className="flex items-center gap-4 text-xs text-muted-foreground">
              <span className="flex items-center gap-1">
                <Clock className="w-3 h-3" />
                {currentAssignment.estimatedDuration}
              </span>
              <span className="flex items-center gap-1">
                <CheckCircle className="w-3 h-3" />
                {currentAssignment.status}
              </span>
            </div>

            <div className="flex gap-2 pt-2">
              <Button className="flex-1 bg-orange-500 hover:bg-orange-600">
                <CheckCircle className="w-4 h-4 mr-2" />
                Complete Task
              </Button>
              <Button variant="outline" className="flex-1 bg-transparent">
                <MessageSquare className="w-4 h-4 mr-2" />
                Report Issue
              </Button>
            </div>
          </CardContent>
        </Card>

        {/* Notifications */}
        <Card>
          <CardHeader className="pb-3">
            <CardTitle className="flex items-center gap-2">
              <Bell className="w-5 h-5 text-orange-500" />
              Recent Notifications
            </CardTitle>
          </CardHeader>
          <CardContent className="space-y-3">
            {notifications.map((notification) => (
              <div
                key={notification.id}
                className={`p-3 rounded-md border ${
                  notification.urgent ? "bg-orange-50 border-orange-200" : "bg-muted/30 border-border"
                }`}
              >
                <div className="flex items-start justify-between">
                  <div className="flex-1">
                    <div className="flex items-center gap-2">
                      <p className="font-medium text-sm">{notification.type}</p>
                      {notification.urgent && (
                        <Badge variant="destructive" className="text-xs bg-orange-500">
                          Urgent
                        </Badge>
                      )}
                    </div>
                    <p className="text-sm text-muted-foreground mt-1">{notification.message}</p>
                  </div>
                  <span className="text-xs text-muted-foreground">{notification.time}</span>
                </div>
              </div>
            ))}
          </CardContent>
        </Card>

        {/* Nearby Incidents */}
        <Card>
          <CardHeader className="pb-3">
            <CardTitle className="flex items-center gap-2">
              <AlertTriangle className="w-5 h-5 text-orange-500" />
              Nearby Incidents
            </CardTitle>
          </CardHeader>
          <CardContent className="space-y-3">
            {nearbyIncidents.map((incident) => (
              <div key={incident.id} className="flex items-center justify-between p-2 rounded-md hover:bg-muted/50">
                <div className="flex items-center gap-3">
                  <div className="w-2 h-2 bg-orange-500 rounded-full"></div>
                  <div>
                    <p className="font-medium text-sm">{incident.type}</p>
                    <p className="text-xs text-muted-foreground">
                      {incident.location} • {incident.distance}
                    </p>
                  </div>
                </div>
                <Badge variant={incident.severity === "Minor" ? "secondary" : "outline"} className="text-xs">
                  {incident.severity}
                </Badge>
              </div>
            ))}
          </CardContent>
        </Card>

        {/* Quick Actions */}
        <Card>
          <CardHeader className="pb-3">
            <CardTitle className="flex items-center gap-2">
              <Radio className="w-5 h-5 text-orange-500" />
              Quick Actions
            </CardTitle>
          </CardHeader>
          <CardContent className="space-y-2">
            <Button variant="outline" className="w-full justify-start bg-transparent">
              <Phone className="w-4 h-4 mr-2" />
              Contact Command Central
            </Button>
            <Button variant="outline" className="w-full justify-start bg-transparent">
              <AlertTriangle className="w-4 h-4 mr-2" />
              Report Emergency
            </Button>
            <Button variant="outline" className="w-full justify-start bg-transparent">
              <Navigation className="w-4 h-4 mr-2" />
              Request Backup
            </Button>
          </CardContent>
        </Card>
      </div>
    </div>
  )
}
